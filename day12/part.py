def build_graph(edges):
    edges = [x.split('-') for x in edges]
    print(edges)

    nodes = {}
    for begin, end in edges:
        if begin not in nodes:
            print(f"adding node {begin}")
            nodes[begin] = []
        if end not in nodes:
            print(f"Adding node {end}")
            nodes[end] = []

        if begin == 'start' or end == 'end':
            nodes[begin].append(end)
        elif end == 'start' or begin == 'end':
            nodes[end].append(begin)
        else:
            nodes[begin].append(end)
            nodes[end].append(begin)

    return nodes


def follow_path(nodes, node_name, path, paths, allow_double_visit, had_double_visit):
    path.append(node_name)
    if node_name == 'end':
        paths.append(path[:])
    else:
        for end_node in nodes[node_name]:
            if end_node not in path:
                follow_path(nodes, end_node, path, paths, allow_double_visit, had_double_visit)
            elif end_node.isupper():
                follow_path(nodes, end_node, path, paths, allow_double_visit, had_double_visit)
            elif allow_double_visit and not had_double_visit:
                follow_path(nodes, end_node, path, paths, allow_double_visit, True)
                
    path.pop()

def main():
    with open('input.txt') as input_file:
        lines = [line.strip() for line in input_file]
        nodes = build_graph(lines)

        path = []
        paths = []
        follow_path(nodes, 'start', path, paths, False, False)
        print(len(paths))

        paths = []
        follow_path(nodes, 'start', path, paths, True, False)
        print(len(paths))


main()
