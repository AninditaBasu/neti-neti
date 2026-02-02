# A Phonological Plausibility Framework for Evaluating Unknown or Ambiguous Symbol Strings

This repository provides a minimal, illustrative Python implementation of the framework described in *Basu, A. (2026). A Phonological Plausibility Framework for Evaluating Unknown or Ambiguous Symbol Strings. Zenodo. https://doi.org/10.5281/zenodo.18450309*. The framework explicitly separates structure from sound, as stated in the abstract of the method note.

> This note proposes a neutral, falsification-oriented framework for evaluating how plausibly a given string of symbols could correspond to spoken language systems at the level of language families. Rather than attempting decipherment or semantic interpretation, the framework assesses phonological *compatibility*: the degree to which a symbol string can be accommodated by known phonological constraints with minimal distortion. The method is intended as an auxiliary tool for hypothesis testing in historical linguistics, undeciphered script studies, and comparative phonology.

-------

This implementation is deliberately simplified and intended for conceptual demonstration only. It shows how
phonological plausibility can be evaluated comparatively, structurally, and transparently, without attempting decipherment, phonetic reconstruction, or semantic interpretation.

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

The sources of strain are labelled and displayed alongside the numeric score for plausibility of the string being realised in a language family.

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

> The name of the repository, `neti-neti`, is inspired from the Upanishads, and embodies the principles of elimination that this framework aims to do.

