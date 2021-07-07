import os

class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        # print(self.graph_dict)

    def get_paths(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graph_dict:
            return []

        all_paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    all_paths.append(p)
        return all_paths

    def get_short_path(self, start, end, path=[]):
        # path = path + [start]

        # if start not in self.graph_dict:
        #     return None
        # if start == end:
        #     return path
        
        # short_paths = None
        # for node in self.graph_dict[start]:
        #     if node not in path:
        #         sp = self.get_short_path(node, end, path)
        #         if sp:
        #             if short_paths is None or len(sp) < len(short_paths):
        #                 short_paths = sp
                        
        # return short_paths

        ''' OR '''
        short_paths = []
        all_paths = self.get_paths(start, end)
        len_paths = [len(i) for i in all_paths]
        try:
            min_len = min(len_paths)
            for i in range(0, len(len_paths)):
                if min_len == len_paths[i]:
                    short_paths.append(all_paths[i])
        except:
            pass
        return short_paths
        


os.system("cls")
routes = [
    ("Mumbai", "Paris"),
    ("Mumbai", "Dubai"),
    ("Paris", "Dubai"),
    ("Paris", "New York"),
    ("Dubai", "New York"),
    ("New York", "Toronto"),
]
route_graph = Graph(routes)
start, end = "Mumbai", "New York"
# print(route_graph.get_paths(start, end))


start, end = "Mumbai", "Toronto"
print("Shortest Path:",route_graph.get_short_path(start, end))