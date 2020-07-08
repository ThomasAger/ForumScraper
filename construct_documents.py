import numpy as np
additional_fn = "07-cheat_"
all_posts = np.load("data/text/"+additional_fn+"all_posts.npy")

all_docs = []

for i in range(len(all_posts)):
    for j in range(len(all_posts[i])):
        doc = ""
        for k in range(len(all_posts[i][j])):
            for n in range(len(all_posts[i][j][k])):
                doc += all_posts[i][j][k][n] + "\n"
        all_docs.append(doc)

np.save("data/docs/"+additional_fn+"all_docs.npy", all_docs)