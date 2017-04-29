from rouge import Rouge

file_name = sys.argv[1]
with codecs.open(file_name, encoding='utf-8') as f:
    hypothesis = f.read().split('\n')
    hypothesis = ' '.join(hypothesis)

file_name2 = sys.argv[2]
with codecs.open(file_name2, encoding='utf-8') as f:
    reference = f.read().split('\n')
    reference = ' '.join(reference)

import pdb; pdb.set_trace()

rouge = Rouge()
scores = rouge.get_scores(reference, hypothesis)
print(scores)
