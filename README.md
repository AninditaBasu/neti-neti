[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18450309.svg)](https://doi.org/10.5281/zenodo.18450309)    [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18495688.svg)](https://doi.org/10.5281/zenodo.18495688)

# A Phonological Plausibility Framework for Evaluating Unknown or Ambiguous Symbol Strings

This repository provides a minimal, illustrative Python implementation of the framework described in *Basu, A. (2026). A Phonological Plausibility Framework for Evaluating Unknown or Ambiguous Symbol Strings. Zenodo. https://doi.org/10.5281/zenodo.18450309*. The framework explicitly separates structure from sound, as stated in the abstract of the method note.

> This note proposes a neutral, falsification-oriented framework for evaluating how plausibly a given string of symbols could correspond to spoken language systems at the level of language families. Rather than attempting decipherment or semantic interpretation, the framework assesses phonological *compatibility*: the degree to which a symbol string can be accommodated by known phonological constraints with minimal distortion. The method is intended as an auxiliary tool for hypothesis testing in historical linguistics, undeciphered script studies, and comparative phonology.

-------

This implementation is deliberately simplified and intended for conceptual demonstration only. It shows how phonological plausibility can be evaluated comparatively, structurally, and transparently, without attempting decipherment, phonetic reconstruction, or semantic interpretation.

The process is this:

```
Symbol string
     ↓
Orthographic parsing
     ↓
Candidate skeletons (possibly many)
     ↓
Phonological evaluation
     ↓
Comparative plausibility scores
```

## Orthographic parsing

Orthographic parsing answers: "Given a string of symbols, what structural hypotheses are reasonable?"

It does not require:

- Knowing the language
- Knowing the meaning
- Knowing the sounds

It produces candidate skeletons, not phonemes. Vowel-less skeletons are permitted at the parsing stage; their markedness is evaluated per phonological profile. Parsing generates candidate skeletons freely (CCCC, CCVCV, etc.). Profiles decide whether CCCC is acceptable, penalised, or highly implausible.

## Skeleton generation

Skeletons are not properties of words. They are hypotheses about how words are structured. That means:

- One symbol string can have multiple skeletons.
- Skeletons can compete.
- Some skeletons are less stable cross-linguistically.

## Phonological evaluation

Phonological evaluation begins only after skeletons exist. It answers: "If this skeleton were to be realised in a given phonological system, how much strain would result?"

It does not care where the skeleton came from. It treats all skeletons equally. It is blind to meaning and orthography.

## Comparative plausibility scores

The sources of strain are labelled and displayed alongside the numeric score for the plausibility of the structure being accommodated by a language-family profile.

Repair diagnostics answer the question: "How would this system typically make it legal?" In other words, if a language family like X were forced to host this structure, what is the kind of repair it would usually perform?

## Quick start

If running from the terminal, type `python cli.py`. 

### Example inputs

The script can be tested with a variety of strings such as these:

- Clear word: `haltemti`
- Consonant-heavy string: `ktbl`
- Mixed ambiguous string: `XQ3M7`
- Purely symbolic string: `◇○◇◆○`

These are intended to illustrate different structural behaviours rather than to suggest any linguistic identification.

### How to read the output

The framework does not identify languages and neither does it recover pronunciations. Instead, it compares how much phonological strain different language-family profiles would experience if forced to accommodate the same structural skeleton.

- A low strain index indicates that the structure is easily accommodated.
- A high strain index indicates that substantial restructuring would be required.
- Plausibility scores are comparative, not absolute.
- Repair diagnostics describe typical adaptation strategies, and not actual historical or phonetic outcomes.

Uniformly high scores across profiles are an indication that the string is unremarkable at this level of abstraction.

--------

## Additional exploratory module: phonological probe

This repository also includes an optional exploratory script, `phonological_probe.py`.

This script is not part of the core plausibility framework described in the preceding paragraphs. It is provided as a sandbox-style extension that demonstrates how the output of the framework might be used to probe possible sound-space constraints, without performing decipherment, phoneme assignment, or semantic interpretation.

The probe exists to answer a very narrow and carefully scoped question:

> Given a structural skeleton that appears phonologically plausible under one or more profiles, what kinds of sound categories could, in principle, occupy each position without violating broad typological constraints?

It does not attempt to:

-  Identify languages
-  Recover pronunciations
-  Assign fixed sound values to symbols
-  Validate real lexical items

If a generated sequence accidentally corresponds to a real word, such a word is explicitly treated as invalid and discarded.


### Conceptual pipeline of the probe

The probe extends the original framework with a strictly gated pipeline:

```
Symbol string
     ↓
Skeleton generation (core framework)
     ↓
Profile plausibility filtering
     ↓
Broad phonological category constraints
     ↓
Pronounceability filters (profile-specific)
     ↓
Entropy-based failure detection
     ↓
Either:
  - Structured sound-category constraints
  - Explicit failure (no safe hypothesis)
```

The probe runs only if at least one phonological profile can host a skeleton with low strain. Otherwise, it fails early and returns no sound hypotheses.

### Broad phonological categories

Instead of phonemes, the probe works with broad sound categories, for example:

```
PHONO_CATEGORIES = {
    "stop": ["b", "d", "g", "k", "t"],
    "fricative": ["s", "ʃ", "x"],
    "sonorant": ["m", "n", "r", "l"]
}
```

These categories are stress probes. They are not sound inventories. They encode resistance patterns (for example, "too many stops in a row") rather than linguistic facts.

Users may extend or modify these categories, but doing so increases the expressive power of the probe and, therefore, its risk of overfitting.

### Profile-specific phonotactic filters

Each phonological profile applies a very conservative pronounceability filter, encoding only broad typological tendencies. These filters are intentionally crude and incomplete. They do not model any real language. 

Examples of encoded constraints include:

-  Resistance to long consonant clusters
-  Preference for CV alternation
-  Tolerance of consonant-only roots
-  Syllable-shape restrictions

The goal is not acceptance, but early rejection.

### Entropy-based failure detection

Entropy is used here informally to describe degrees of freedom.  After constraints are applied, the probe measures how much freedom remains in the sound-space. A high entropy indicates that almost anything is still possible, while a low entropy indicates that several possibilities have been eliminated.

The probe declares a failure if:

-  Too many positions collapse to a single category, or
-  Too few viable combinations survive filtering,

This prevents the system from:

-  Hallucinating precision
-  Converging prematurely on a single "reading"
-  Producing outputs that look specific but are unjustified

A failure result is considered a successful safeguard, not an error.

### How to run the probe

From the terminal, run: `python cli_probe.py`.

The probe reports EITHER structured, profile-conditional sound-category constraints OR an explicit failure message explaining why sound generation was not safe.

### Cautionary note

This probe is illustrative only. It exists to show how a falsification-oriented plausibility framework can be extended without crossing into decipherment.

Users interested in extending this module should do so carefully, and treat all outputs as non-linguistic scaffolding and not as hypotheses about real languages.

--------

```
The name of the repository, `neti-neti`, is inspired from the Brihadaranyak Upanishad (2.3.6), and embodies the principles of elimination that this framework aims to do. 

"अथात आदेशः नेति नेति, न ह्येतस्मादिति नेत्यन्यत्परमस्ति;"
 
"Now therefore the description: 'Not this, not this'. Because there is no other and more appropriate description than this 'Not this'. "

```
