from embedding_en import *
from glob import glob
from scipy import spatial
import sys


def cos_sim(a,b):
  return 1 - spatial.distance.cosine(a, b)

def semantic_retrieval(question, input_txt_dir, input_vec_dir, candidate=10):
  file_list = glob(input_vec_dir+'/*txt')
  list_vec = []
  q_embed = get_embed(question)
  for ll in file_list:
    txt_name = input_txt_dir + '/'+ ll.split('/')[-1]
    txt = open(txt_name).read()
    vec = eval(open(ll).read())
    score = cos_sim(vec,q_embed)
    list_vec.append((txt,score))

  list_vec.sort(key=lambda x:x[1], reverse=True)
  result = []
  for lstv in list_vec[:candidate]:
    result.append(lstv[0])

  return result


if __name__ == '__main__':
  input_txt_dir = sys.argv[1] #doc_vec/txts/
  input_vec_dir = sys.argv[2] #doc_vec/vecs/
  question = sys.argv[3]
  search = semantic_retrieval(question, input_txt_dir, input_vec_dir)
  print(search)
