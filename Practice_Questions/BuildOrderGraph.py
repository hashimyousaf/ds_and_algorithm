def createGraph(projects, dependencies):
    projectGraph = {}
    for project in projects:
        projectGraph[project] = []
    for pairs in dependencies:
        projectGraph[pairs[0]].extend(pairs[1])
    return projectGraph

project = ['a', 'b', 'c', 'd', 'e', 'f']
dependencies = [('a','d'), ('f','b'), ('b','d'), ('f','a'), ('d','c')]

project_graph = createGraph(project, dependencies)

def builder_utility(proj, stack, visited):
    visited.append(proj)
    for project in project_graph[proj]:
        if project not in visited:
            builder_utility(project, stack, visited)
    stack.insert(0, proj)

def findBuildOrder(projects):
    visited = []
    stack = []
    for project in projects:
        if project not in visited:
            builder_utility(project, stack, visited)
    return stack



def findBuildOrderIterative(projects):
    # Not the right implementation
    visited = []
    for project in projects:
        stack = [project]
        while stack:
            current = stack.pop();
            if current not in visited:
                visited.insert(0, current)
            for dependant  in project_graph[current]:
                if dependant not in visited:
                    stack.append(dependant)


    return visited


# print(findBuildOrderIterative(project))
print(findBuildOrder(project))