import numpy as np
import util as u
one_p = u.import1dArray("data/8 illusztr.txt")
all_p = u.import1dArray("data/all/all_paragraphs.txt")

buddha_id = []
not_buddha_id = []

classes = []
for i in range(len(all_p)):
    if "buddha" in all_p[i] or "Buddha" in all_p[i]:
        buddha_id.append(i)
        classes.append(1)
    else:
        not_buddha_id.append(i)
        classes.append(0)

buddha_p = all_p[buddha_id]

not_buddha_p = all_p[not_buddha_id]

np.savetxt("data/classes/classes.txt", classes, encoding="utf-8", fmt='%s')
np.savetxt("data/classes/buddha.txt", buddha_p, encoding="utf-8", fmt='%s')
np.savetxt("data/classes/not_buddha.txt", not_buddha_p, encoding="utf-8", fmt='%s')