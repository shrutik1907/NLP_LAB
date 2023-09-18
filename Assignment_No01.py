# Name-Shrutik Laxman Hon
# Batch-B2
# Roll no-26
# Title- Assignment based on text pre-processing using NLP operations-tokenization,stop words,lemitization and part of speech tagging

import spacy
nlp = spacy.load("en_core_web_sm")
about_text = (
    "Wavelet soft-threshold de-noising method was applied to preprocess the noisy signal,"
     "and the noise interference in disturbance detection was reduced to a great extent."
)
about_doc = nlp(about_text)

for token in about_doc:
    print (token, token.idx)


# Wavelet 0
# soft 8
# - 12
# threshold 13
# de 23
# - 25
# noising 26
# method 34
# was 41
# applied 45
# to 53
# preprocess 56
# the 67
# noisy 71
# signal 77
# , 83
# and 84
# the 88
# noise 92
# interference 98
# in 111
# disturbance 114
# detection 126
# was 136
# reduced 140
# to 148
# a 151
# great 153
# extent 159
# . 165

#Stop words

spacy_stopwords = spacy.lang.en.stop_words.STOP_WORDS
len(spacy_stopwords)

print([token for token in about_doc if not token.is_stop])

# [Wavelet, soft, -, threshold, de, -, noising, method, applied, preprocess, noisy, signal, ,, 
#  noise, interference, disturbance, detection, reduced, great, extent, .]

#Lemmitization
nlp = spacy.load("en_core_web_sm")
conference_help_text = (
     "Wavelet soft-threshold de-noising method was applied to preprocess the noisy signal,"
     "and the noise interference in disturbance detection was reduced to a great extent."
)
conference_help_doc = nlp(conference_help_text)
for token in conference_help_doc:
    if str(token) != str(token.lemma_):
        print(f"{str(token):>20} : {str(token.lemma_)}")


# Wavelet : wavelet
#      was : be
#  applied : apply
#      was : be
#  reduced : reduce

#Part of Speech Tagging

nlp = spacy.load("en_core_web_sm")
about_text = (
     "Wavelet soft-threshold de-noising method was applied to preprocess the noisy signal,"
     "and the noise interference in disturbance detection was reduced to a great extent."
)
about_doc = nlp(about_text)
for token in about_doc:
    print(
        f"""
TOKEN: {str(token)}
=====
TAG: {str(token.tag_):10} POS: {token.pos_}
EXPLANATION: {spacy.explain(token.tag_)}"""
    )



# TOKEN: Wavelet
# =====
# TAG: NN         POS: NOUN
# EXPLANATION: noun, singular or mass

# TOKEN: soft
# =====
# TAG: JJ         POS: ADJ
# EXPLANATION: adjective (English), other noun-modifier (Chinese)

# TOKEN: -
# =====
# TAG: HYPH       POS: PUNCT
# EXPLANATION: punctuation mark, hyphen

# TOKEN: threshold
# =====
# TAG: NN         POS: NOUN
# EXPLANATION: noun, singular or mass

# TOKEN: de
# =====
# TAG: JJ         POS: ADJ
# EXPLANATION: adjective (English), other noun-modifier (Chinese)

# TOKEN: -
# =====
# TAG: JJ         POS: ADJ
# EXPLANATION: adjective (English), other noun-modifier (Chinese)

# TOKEN: noising
# =====
# TAG: JJ         POS: ADJ
# EXPLANATION: adjective (English), other noun-modifier (Chinese)

# TOKEN: method
# =====
# TAG: NN         POS: NOUN
# EXPLANATION: noun, singular or mass

# TOKEN: was
# =====
# TAG: VBD        POS: AUX
# EXPLANATION: verb, past tense

# TOKEN: applied
# =====
# TAG: VBN        POS: VERB
# EXPLANATION: verb, past participle

# TOKEN: to
# =====
# TAG: TO         POS: PART
# EXPLANATION: infinitival "to"

# TOKEN: preprocess
# =====
# TAG: VB         POS: VERB
# EXPLANATION: verb, base form

# TOKEN: the
# =====
# TAG: DT         POS: DET
# EXPLANATION: determiner

# TOKEN: noisy
# =====
# TAG: JJ         POS: ADJ
# EXPLANATION: adjective (English), other noun-modifier (Chinese)

# TOKEN: signal
# =====
# TAG: NN         POS: NOUN
# EXPLANATION: noun, singular or mass

# TOKEN: ,
# =====
# TAG: ,          POS: PUNCT
# EXPLANATION: punctuation mark, comma

# TOKEN: and
# =====
# TAG: CC         POS: CCONJ
# EXPLANATION: conjunction, coordinating

# TOKEN: the
# =====
# TAG: DT         POS: DET
# EXPLANATION: determiner

# TOKEN: noise
# =====
# TAG: NN         POS: NOUN
# EXPLANATION: noun, singular or mass

# TOKEN: interference
# =====
# TAG: NN         POS: NOUN
# EXPLANATION: noun, singular or mass

# TOKEN: in
# =====
# TAG: IN         POS: ADP
# EXPLANATION: conjunction, subordinating or preposition

# TOKEN: disturbance
# =====
# TAG: NN         POS: NOUN
# EXPLANATION: noun, singular or mass

# TOKEN: detection
# =====
# TAG: NN         POS: NOUN
# EXPLANATION: noun, singular or mass

# TOKEN: was
# =====
# TAG: VBD        POS: AUX
# EXPLANATION: verb, past tense

# TOKEN: reduced
# =====
# TAG: VBN        POS: VERB
# EXPLANATION: verb, past participle

# TOKEN: to
# =====
# TAG: IN         POS: ADP
# EXPLANATION: conjunction, subordinating or preposition

# TOKEN: a
# =====
# TAG: DT         POS: DET
# EXPLANATION: determiner

# TOKEN: great
# =====
# TAG: JJ         POS: ADJ
# EXPLANATION: adjective (English), other noun-modifier (Chinese)

# TOKEN: extent
# =====
# TAG: NN         POS: NOUN
# EXPLANATION: noun, singular or mass

# TOKEN: .
# =====
# TAG: .          POS: PUNCT
# EXPLANATION: punctuation mark, sentence closer