"""
Phonological probing layer with profile-specific filters and entropy-based failure detection.

This module is an extension of the plausibility framework:
- No lexicon
- No semantics
- No readings
- Pseudo-forms are disposable scaffolding only
"""

from itertools import product
from collections import defaultdict
from phonological_plausibility_demo import analyse_string

# --------------------------------------------------
# Broad phonological categories (stress probes)
# --------------------------------------------------

PHONO_CATEGORIES = {
    "stop": ["b", "d", "g", "k", "t"],
    "fricative": ["s", "ʃ", "x"],
    "sonorant": ["m", "n", "r", "l"]
}

CATEGORY_NAMES = set(PHONO_CATEGORIES.keys())

ALL_SOUNDS = [
    (cat, sound)
    for cat, sounds in PHONO_CATEGORIES.items()
    for sound in sounds
]

# --------------------------------------------------
# Profile-specific pronounceability filters
# --------------------------------------------------

def pronounceable(sequence, profile):
    """
    Broad phonotactic stress filters.
    These encode resistance patterns, not real phonology.
    """

    cats = [cat for cat, _ in sequence]
    length = len(cats)

    # Universal sanity checks
    if length >= 3:
        for i in range(length - 2):
            if cats[i] == cats[i+1] == cats[i+2]:
                return False  # triple repetition is bad everywhere

    # Profile-specific resistance
    if profile == "Semitic-like":
        # Dislike all-fricative sequences
        if all(cat == "fricative" for cat in cats):
            return False

    elif profile == "Indo-European-like":
        # Very tolerant, but still dislikes extreme homogeneity
        if cats.count("sonorant") == length:
            return False

    elif profile == "Austronesian-like":
        # Strong CV rhythm: clusters are hostile
        if length > 1:
            return False  # consonant clusters rejected outright

    elif profile == "Sinitic-like":
        # Extremely restrictive syllable shapes
        if length > 1:
            return False

    return True


# --------------------------------------------------
# Generate pronounceable pseudo-forms
# --------------------------------------------------

def generate_pseudo_forms(skeleton, profile, max_forms=100):
    """
    Generate pronounceable nonsense forms for a skeleton
    under a given phonological profile.
    """

    slots = []
    for char in skeleton:
        if char == "C":
            slots.append(ALL_SOUNDS)
        else:
            # Vowels are NOT probed; they carry no constraints here
            slots.append([("vowel", "V")])

    results = []
    for combo in product(*slots):
        if pronounceable(combo, profile):
            results.append(combo)
        if len(results) >= max_forms:
            break

    return results


# --------------------------------------------------
# Collapse pseudo-forms into positional constraints
# --------------------------------------------------

def collapse_constraints(pseudo_forms, skeleton):
    """
    Reduce pseudo-forms to positional phonological constraints.
    """

    constraints = defaultdict(set)

    for form in pseudo_forms:
        for i, (cat, _) in enumerate(form):
            if skeleton[i] == "C":
                constraints[i].add(cat)

    return constraints


# --------------------------------------------------
# Entropy-based failure detection
# --------------------------------------------------

def entropy_ratio(constraints):
    """
    Informal entropy metric:
    remaining possibilities / maximum possibilities
    """

    total = 0
    max_total = 0

    for cats in constraints.values():
        total += len(cats)
        max_total += len(CATEGORY_NAMES)

    if max_total == 0:
        return 1.0

    return total / max_total


def is_failure(constraints, entropy_threshold=0.8):
    """
    Decide whether probing produced meaningful information.
    """

    if not constraints:
        return True

    ratio = entropy_ratio(constraints)
    return ratio >= entropy_threshold


# --------------------------------------------------
# Main probing function
# --------------------------------------------------

def probe_string(symbol_string, strain_threshold=1):
    """
    End-to-end safe probing:
    - filters profiles by plausibility
    - probes phonological affordances
    - stops on failure
    """

    analysis = analyse_string(symbol_string)

    surviving_profiles = [
        e["family"]
        for e in analysis["evaluations"]
        if e["strain"] <= strain_threshold
    ]

    if not surviving_profiles:
        return {
            "status": "FAILURE",
            "reason": "No phonological profile can host this structure"
        }

    results = []

    for profile in surviving_profiles:
        for skeleton in analysis["skeletons"]:
            pseudo_forms = generate_pseudo_forms(skeleton, profile)

            if not pseudo_forms:
                continue

            constraints = collapse_constraints(pseudo_forms, skeleton)

            if is_failure(constraints):
                results.append({
                    "profile": profile,
                    "skeleton": skeleton,
                    "status": "FAILURE",
                    "reason": "High entropy (low information gain)"
                })
            else:
                results.append({
                    "profile": profile,
                    "skeleton": skeleton,
                    "status": "SUCCESS",
                    "entropy_ratio": round(entropy_ratio(constraints), 3),
                    "constraints": {
                        f"position_{i}": sorted(list(cats))
                        for i, cats in constraints.items()
                    }
                })

    if not results:
        return {
            "status": "FAILURE",
            "reason": "No discriminative constraints produced"
        }

    return {
        "status": "OK",
        "results": results
    }
