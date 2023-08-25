
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_string = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert_string(self, word):
        current = self.root
        for i in word:
            ch = i
            node = current.children.get(ch)
            if node == None:
                node = TrieNode()
                current.children.update({ch: node})
            current = node
        current.end_of_string = True
        print("Successfully inserted")
        # Time and space comlexity is O(m) where m is length of the word we want to insert
        # why space = O(m), because if word does not exist in worst case, we have to make node of every character.

    def search_string(self, word):
        current = self.root
        for i in word:
            ch = i
            node = current.children.get(ch)
            if node is None:
                return False
            current = node
        if current.end_of_string == True:
            return True
        else:
            return False

def delete_string(root, word, index):
    character = word[index]
    curren_node = root.children.get(character)
    can_this_node_be_deleted = False

    if len(curren_node.children) > 1:
        delete_string(curren_node, word, index+1)
        return False

    if index == len(word) -1:
        if len(curren_node.children) >= 1:
            curren_node.end_of_string = False
            return False
        else:
            root.children.pop(ch)
            return True

    if curren_node.end_of_string == True:
        delete_string(curren_node, word, index+1)
        return False

    can_this_node_be_deleted = delete_string(curren_node, word, index+1)
    if can_this_node_be_deleted == True:
        root.children.pop(character)
        return True
    else:
        return False


new_trie = Trie()
new_trie.insert_string("APP")
new_trie.insert_string("APPL")
#delete_string(new_trie.root, "APP", 0)
print(new_trie.search_string("APP"))
