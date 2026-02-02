# Minimal, illustrative implementation of the Phonological Plausibility Framework.
# Core logic only. Returns structured data.

from itertools import product

# --------------------------------------------------
# Stage 1: Orthographic parsing to skeletons
# --------------------------------------------------

def parse_orthography(symbol_string):
    """
    Given an input string, generate multiple plausible CV skeletons.

    This function:
    - does NOT assume a known language
    - allows ambiguity (multiple skeletons)
    - keeps decisions structural, not phonetic
    """
    symbol_string = symbol_string.lower()
    vowels = set("aeiou")
    ambiguous_digraphs = {"dh", "th", "kh", "ph", "bh"}

    # Step 1: Segment the string into units
    units = []
    i = 0
    while i < len(symbol_string):
        if symbol_string[i:i+2] in ambiguous_digraphs:
            units.append(symbol_string[i:i+2])
            i += 2
        else:
            units.append(symbol_string[i])
            i += 1

    # Step 2: For each unit, list possible C/V roles
    role_options = []
    for unit in units:
        options = set()
        if any(char in vowels for char in unit):
            options.add("V")
        options.add("C")
        role_options.append(options)

    # Step 3: Generate all combinations of roles
    skeletons = set()
    for combination in product(*role_options):
        skeleton = "".join(combination)
        if "V" not in skeleton:
            # optionally keep vowel-less skeletons for repair evaluation
            skeletons.add(skeleton)
        else:
            skeletons.add(skeleton)

    return skeletons

# --------------------------------------------------
# Stage 2: Family-level phonological profiles
# --------------------------------------------------

phonological_profiles = {
    "Indo-European-like": {
        "max_onset_cluster": 3,
        "allows_vowel_initial": True,
        "repair_cost": 1,
        "repairs": {
            "onset_cluster": "consonant cluster tolerated or reduced",
            "vowel_less": "default vowel insertion"
        }
    },
    "Austronesian-like": {
        "max_onset_cluster": 1,
        "allows_vowel_initial": True,
        "repair_cost": 2,
        "repairs": {
            "onset_cluster": "vowel epenthesis between consonants",
            "vowel_less": "systematic vowel insertion"
        }
    },
    "Semitic-like": {
        "max_onset_cluster": 2,
        "allows_vowel_initial": False,
        "repair_cost": 1,
        "repairs": {
            "onset_cluster": "templatic reanalysis",
            "vowel_less": "vowels supplied by morphological pattern"
        }
    },
    "Sinitic-like": {
        "max_onset_cluster": 1,
        "allows_vowel_initial": False,
        "repair_cost": 3,
        "repairs": {
            "onset_cluster": "vowel insertion or syllable splitting",
            "vowel_less": "not well-formed; heavy restructuring"
        }
    }
}

# --------------------------------------------------
# Stage 3: Evaluation
# --------------------------------------------------

def evaluate_skeleton(skeleton, profile):
    """
    Return a strain score and repair diagnostics for a skeleton
    under a given language-family profile.
    """
    strain = 0
    diagnostics = []

    # Check vowel-less skeleton
    if "V" not in skeleton:
        cost = profile["repair_cost"]
        strain += cost
        diagnostics.append(
            f"Vowel-less structure (+{cost}) → repair: {profile['repairs']['vowel_less']}"
        )

    # Check vowel-initial
    if skeleton.startswith("V") and not profile["allows_vowel_initial"]:
        cost = profile["repair_cost"]
        strain += cost
        diagnostics.append(
            f"Vowel-initial form (+{cost}) → repair: initial vowel suppression or glide insertion"
        )

    # Check onset cluster length
    onset = ""
    for char in skeleton:
        if char == "C":
            onset += char
        else:
            break

    excess = len(onset) - profile["max_onset_cluster"]
    if excess > 0:
        cost = excess * profile["repair_cost"]
        strain += cost
        diagnostics.append(
            f"Onset cluster too long by {excess} (+{cost}) → repair: {profile['repairs']['onset_cluster']}"
        )

    return strain, diagnostics

# --------------------------------------------------
# Stage 4: Core function to return structured results
# --------------------------------------------------

def analyse_string(word):
    """
    Analyse a string and return:
    - skeleton hypotheses
    - evaluation results for each language family
    """
    results = {
        "input": word,
        "skeletons": parse_orthography(word),
        "evaluations": []
    }

    for family, profile in phonological_profiles.items():
        best_strain = None
        best_diagnostics = None

        for skeleton in results["skeletons"]:
            strain, diagnostics = evaluate_skeleton(skeleton, profile)
            if best_strain is None or strain < best_strain:
                best_strain = strain
                best_diagnostics = diagnostics

        results["evaluations"].append({
            "family": family,
            "strain": best_strain,
            "plausibility": max(1, 5 - best_strain),
            "diagnostics": best_diagnostics
        })

    return results

# A terminal-friendly function
def run_demo(word):
    """Return a string suitable for printing in CLI"""
    results = analyse_string(word)
    lines = []
    lines.append(f"Input string: {results['input']}")
    lines.append(f"Generated skeletons: {results['skeletons']}")
    for entry in results["evaluations"]:
        lines.append("")
        lines.append(f"{entry['family']}")
        lines.append(f"  Strain index: {entry['strain']}")
        lines.append(f"  Plausibility score (1–5): {entry['plausibility']}")
        if entry["diagnostics"]:
            lines.append("  Diagnostics:")
            for d in entry["diagnostics"]:
                lines.append(f"   - {d}")
        else:
            lines.append("  Diagnostics: none")
    return "\n".join(lines)
