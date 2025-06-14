import sys

doc = open(sys.argv[1]).read()
output_dir = sys.argv[2]  #"doc_vec/txts/"

def fixed_size_chunking_with_overlap(text, chunk_size, overlap):
  words = text
  chunks = []
  start = 0
  
  while start < len(words):
    end = start + chunk_size
    chunk = words[start:end]
    chunks.append(chunk)
    start += chunk_size - overlap
  
  return chunks

chunks = fixed_size_chunking_with_overlap(doc, 200, 20)

#print(chunks)
for i,ch in enumerate(chunks):
  file_name = 'chunk_%d.txt'%i
  opt = open(output_dir+'/'+file_name,'w')
  opt.write(ch)
  opt.close()
