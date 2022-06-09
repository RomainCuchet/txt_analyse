alphabet = [chr(97+i) for i in range(26)]
print(alphabet)
txt_file = ''
def cipher_analyse(txt_file):
    nb_letter = 0
    dict = {}
    txt_file = txt_file.lower()
    for i in alphabet:
        count = txt_file.count(i)
        nb_letter += count
        dict.update({i:count})
    dict.update({'len':nb_letter})
    return dict

def print_insight(dict):
    len = dict.get('len')
    del dict['len']
    for i in dict:
        print(i + ': {} %'.format(round((dict.get(i)/len)*100),1))
