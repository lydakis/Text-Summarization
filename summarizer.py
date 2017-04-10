class Summarizer(object):
    def __init__(self, clusters):
        self.clusters = clusters

    def generate(self):
        biggest_cl = max([(len(v), k) for k, v in self.clusters.items()],
                        key=lambda x: x[0])[1]
        sentences = sorted([(i, s) for s, (_, i) in self.clusters[biggest_cl].items()],
                    key=lambda x: x[0])
        return ''.join([s for _, s in sentences])
