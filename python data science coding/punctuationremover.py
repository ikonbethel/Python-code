#simple decorator for text manipulator
#python for data science learning
#created by ikon beth
#DevCUyo100DaysOfCode

from string import punctuation

def pipeline_wrapper(func):
    def to_lower(x):
        return x.lower()

    def remove_punc(x):
        for p in punctuation:
            x = x.replace(p, '')
        return x

    def wrapper(*args, **kwargs):
        x = to_lower(*args, **kwargs)
        x = remove_punc(x)
        return func(x)
    return wrapper

@pipeline_wrapper
def tokenize_whitespace(inText):
    return inText.split()

s = 'string. WiTh. PUNctuation?'
print (tokenize_whitespace(s))
