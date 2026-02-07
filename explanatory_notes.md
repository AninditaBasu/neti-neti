# Phonological plausibility

----------------

This framework is falsification-oriented (hence the repository name of *neti, neti*, which is a concept from the Upanishads meaning *not this, not this*).  

This framework computes the degree to which the *structure* of a symbol string can be accommodated by a *phonological profile*. It therefore makes no claim about what a string means, what it sounded like, or whether it corresponds to any known language. No attempt whatsoever is made to use phonetic substitution, acoustic similarity, or feature-based correspondence.

----------------

## Phonological profile

A phonological profile, in the context of this framework, is **neither** a language **nor** a language family. What it actually is can be best described if you imagine a set of compromises or tolerances that a group of languages exhibit when they are forced to host or carry or accommodate a symbol string of unknown sounds. A phonological profile answers questions such as these:

- How allergic is this system to consonant clusters?
- Does it tolerate vowel-less words?
- Does it prefer a `CV` rhythm?
- When something un-hostable is encountered, how does the system try to fix it?

Thus, instead of being something absolute, a profile is rather probabilistic because it is about behaviour in an unknown situation (stress). "Probabilistic" here does not mean statistically inferred from data, but typologically motivated. Profiles collect the kinds of repairs that languages of a certain type are known to use when forced to accommodate unfamiliar structures.

Phonological profiles draw inspiration from language families in their attributes. These attributes are intentionally high-level and abstracted. They describe structural tolerances, rather than phonetic features or a list of actual speech-sounds.

### Profile attributes

Each phonological profile is defined by a small set of high-level attributes:

- Structural tolerances, for example, maximum onset or coda cluster length
- Vowel dependency, for example, whether vowel-less skeletons are tolerated or repaired
- Positional constraints, for example, allowing of vowel-initial or consonant-final forms
- Repair preferences, for example, vowel epenthesis, cluster simplification, templatic reinterpretation

These attributes are intentionally abstract and do not encode specific sounds, phonemes, or phonetic features.

### CV-oriented systems and templatic systems

CV-oriented systems organise words around syllabic rhythm, typically favouring consonant–vowel alternation. To these systems, lengthy consonant clusters seem out of place. When a word has too many consonants one after the other, these systems attempt to repair the word by inserting vowels (epenthesis) so that it can obtain a smoother rhythm. In such systems, each additional consonant in a consonant-cluster increases structural pressure, resulting in cumulative strain.

Templatic systems, by contrast, organise words around abstract patterns or templates into which consonants are inserted.The consonant sequence itself often carries the core meaning. Vowels are added later according to grammatical rules rather than the vowels being part of the basic identity of the word. Because of this, words with many consonants in a row are not automatically problematic. Instead of needing a repair like adding vowels, the word can simply be interpreted as fitting a different overall pattern. 

### Example profiles

Phonological systems differ in predictable, family-level ways when forced to host or accommodate unfamiliar structures. These labels are mnemonic conveniences rather than claims about historical identity. This framework classifies no input string ever as being a member of any family.

1. Indo-European-like (cluster-tolerant)

-  Examples: Sanskrit, Greek, Slavic, Germanic
-  Traits:
    -  Allows complex onsets and codas
    -  Consonant-heavy words possible
    -  Repairs are often minimal
- Behaviour under stress: "Try to keep the structure; tolerate clusters."

2. Semitic-like (root-templatic)

-  Examples: Arabic, Hebrew
-  Traits:
    -  Consonant sequences meaningful
    -  Vowels supplied by morphology
    -  Skeletons can be consonant-only
-  Behaviour under stress: "Interpret consonants as roots; infer vowels."

3. Austronesian-like (CV-preferential)

-  Examples: Malay, Hawaiian, Tagalog
-  Traits:
    - Strong CV rhythm
    - Minimal clusters
    - Vowel insertion is systematic
-  Behaviour under stress: "Break it up; insert vowels everywhere."

4. Sinitic-like (syllable-restricted)

-  Examples: Mandarin, Cantonese
-  Traits:
    - Very limited syllable shapes
    - Few codas
    - Strong restructuring under stress
-  Behaviour under stress: "Reshape aggressively; syllabify strictly."

Profiles are stress-testers that measure the comparative strain that they must endure (the degree to which they must bend) to accommodate the structure of a symbol string. 

They attempt to answer the question: "Can Profile A accommodate StringXStructure? Not this, not this." The framework advances by elimination. Profiles that need excessive distortion are progressively ruled out.

They also attempt to answer the question: "If forced to accommodate StringXStructure, how will Profile A have to bend? By inserting vowels? By splitting clusters? By adding or removing slots? How can this *skeleton* be carried?"

----------------

## Skeletons

A skeleton, in the context of this framework, is a hypothesis about the structure of a given symbol string. It defines syllable structure and expected morpheme length. For example, `CCVCC` is a skeleton that assumes a structure in which a vowel slot intervenes between consonant slots, regardless of whether any symbol in the string directly corresponds to a vowel.

A skeleton, when passed through the filter of a phonological profile, can answer questions such as:

- This profile is unlikely to encode consonant clusters.
- This system behaves like a CV-heavy language.
- These sequences are implausible as Indo-European phonology.
- This looks more like a suffixing language than isolating.

----------------

## Repair costs and strain

Repair costs, in this framework, are neither empirical weights learnt from data, nor do they represent phonetic difficulty or cognitive effort. Instead, they encode relative structural resistance: given its typological tendencies, how strongly does a phonological system resists (or bends to) a particular kind of violation.

A repair cost reflects the degree of reorganisation required for a system to accommodate an otherwise ill-formed structure. For example, in strongly CV-preferential systems, each additional consonant in a cluster typically forces vowel insertion and syllable restructuring, resulting in cumulative strain. In contrast, in templatic or cluster-tolerant systems, similar violations may be absorbed with minimal reinterpretation (and thus carry a lower repair cost).

Repair costs are intended to be interpreted ordinally (higher strain versus lower strain), not metrically. They indicate more structural pressure or less structural pressure, and not precise degrees of likelihood. The numeric values for strain used in a subsequent section (titled `Worked example`) is not to be interpreted quantitatively because their role is to enable comparative ranking across profiles, make strain accumulation transparent, and support falsification by highlighting incompatibilities.

----------------

## Scoring

Given skeleton `S`, which phonological profiles are strained or unstrained? The scoring might be something like the following tables. The values are illustrative in nature. Exact scores depend on profile parameters.

Table 1. Symbol strings and candidate skeletons

| Input string | Notes                                                           | Candidate skeletons |
| ------------ | ------------------------------------------- | --------------------- |
| dhruva        | Ambiguous digraph, vowel letters present | CCVCV, CVCVC |
| ktbl             | Consonant-only Latin string                        | CCCC  |
| ◇○◇◆○   | Pure symbol string                                       | CCCCC   |
| 𒀸𒀸𒁹         | Cuneiform-like symbols                                | CCC   |
| pa-ta          | Hyphenated, segmented                              | CVCV  |

Identical skeletons receive identical evaluations under a given profile. Differences in plausibility arise only when a symbol string has more than one possible skeleton. The string `dhruva` yields two candidate skeletons (`CCVCV` and `CVCVC`). These skeletons are evaluated independently against phonological profiles. Differences in plausibility arise not from the symbol string itself, but from the structural commitments implied by each skeleton.

Table 2. Skeleton-centric phonological plausibility

| Skeleton | Indo-European-like                     | Semitic-like                                      | Austronesian-like                          |
| --------- | --------------------------------- | ----------------------------------- | ----------------------------------- |
| CCC      | Strain: 1<br>Repair: tolerate cluster  | Strain: 0<br>Repair: consonantal root             | Strain: 4<br>Repair: vowel insertion       |
| CCCC     | Strain: 2<br>Repair: cluster reduction | Strain: 1<br>Repair: templatic mapping            | Strain: 6<br>Repair: systematic epenthesis |
| CCCCC    | Strain: 3<br>Repair: reduce clusters   | Strain: 2<br>Repair: root-template interpretation | Strain: 8<br>Repair: vowel insertion       |
| CCVCV    | Strain: 0<br>Repair: none              | Strain: 1<br>Repair: vowel alignment              | Strain: 1<br>Repair: CV smoothening          |
| CVCVC    | Strain: 0<br>Repair: none              | Strain: 1<br>Repair: templatic reanalysis         | Strain: 0<br>Repair: none                  |


## Worked examples

Here are two examples to show how the framework operates on two contrasting inputs:

1. A symbol string with no phonetic or orthographic cues
2. A letter string whose orthography permits multiple structural interpretations

The purpose is to demonstrate structural abstraction and comparative evaluation, not to suggest historical or linguistic identification.

### Worked example 1: Cuneiform-like symbol string

Consider the input string `𒀸𒀸𒁹`.

#### Step 1: Orthographic parsing

The symbols are treated as abstract marks with no assumed sound values. None of the symbols is intrinsically vowel-like, and no segmentation cues are available. The parser therefore generates the structural hypothesis `CCC`.

This skeleton represents a consonant-only structure. Other interpretations are possible in principle, but this example yields a single dominant hypothesis.

#### Step 2: Skeleton evaluation against profiles

The skeleton `CCC` is evaluated independently by each phonological profile.

**Indo-European-like profile**

- Consonant clusters are tolerated
- Vowel-less forms are marked but possible

Evaluation:
- Onset cluster length within tolerance
- Vowel-less structure mildly marked

Total strain: low

Interpretation: The structure could be accommodated with minimal adjustment, potentially as a consonant-heavy word or stem.

**Semitic-like profile**

- Consonantal skeletons are well-formed
- Vowels supplied by morphological templates

Evaluation:
- No structural violation detected

Total strain: minimal

Interpretation: The structure is compatible with root-based morphology and requires no direct repair.

**Austronesian-like profile**

- Strong preference for CV rhythm
- Consonant clusters disfavoured

Evaluation:
- Vowel-less structure detected
- Cluster length exceeds tolerance

Total strain: high

Interpretation: The system would need to insert vowels to break up the cluster, resulting in substantial restructuring.

### Worked example 2: Orthographic string

Consider the input string `dhruva`.

This example is included not because its language is known, but because its orthography allows multiple structural interpretations.

#### Step 1: Orthographic parsing

The parser identifies ambiguity in the string:

- The digraph `dh` may function as a single consonantal unit or as two separate consonants.
- The letters `u` and `a` may function as vowel slots.

As a result, the parser generates multiple candidate skeletons:

- `CCVCV`
- `CVCVC`

These skeletons represent competing structural hypotheses derived from the same symbol string.

#### Step 2: Skeleton evaluation against profiles

Each skeleton is evaluated independently.

**Skeleton: `CCVCV`**

- Indo-European-like profile: low strain (complex onset tolerated)
- Semitic-like profile: moderate strain (vowel positioning may be reinterpreted)
- Austronesian-like profile: moderate strain (cluster smoothing or vowel adjustment)

**Skeleton: `CVCVC`**

- Indo-European-like profile: minimal strain
- Semitic-like profile: moderate strain (templatic reinterpretation)
- Austronesian-like profile: minimal strain (strong CV rhythm)

#### Summary

The framework does not select a "correct" skeleton. Instead, it shows that different structural hypotheses interact differently with different phonological profiles.

These examples are for demonstrating two core principles of the framework:

- Structural ambiguity is preserved rather than resolved prematurely.
- Plausibility is assessed comparatively, not absolutely.

At no point is sound reconstruction or semantic interpretation invoked.

------------

## Clarifications and non-goals

1. This is not decipherment.

This framework does not attempt to identify languages, reconstruct phonemes, or assign meanings. High plausibility does not imply historical, genealogical, or semantic connection.

2. Skeletons are hypotheses.

A skeleton is a structural hypothesis derived from a symbol string. Multiple skeletons may coexist, and the framework does not select a uniquely correct one. A skeleton is not a discovery.

3. Profiles are abstractions.

Phonological profiles are typologically motivated abstractions. They are inspired by language families but are not intended to model any specific language or proto-language. Profiles are not families.

4. Repair descriptions are illustrative.

Repair diagnostics describe types of structural accommodation. They do not describe actual historical sound changes or loanword adaptation paths.

5. Scores are comparative.

Strain and plausibility scores are meaningful only in comparison across profiles for the same skeleton. They are not probabilities or likelihood estimates. They are not absolute.

6. Symbol identity is discarded early.

Once structural abstraction is performed, symbol identity plays no role in evaluation. Apparent patterns in glyph shape or repetition are not interpreted phonologically.

------------

