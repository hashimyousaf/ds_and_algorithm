"""sentence = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
word_count = 1
current_line_length = 0
current_line_list = []
max_width = 20

for word in sentence:
   if (current_line_length + (word_count-1) + len(word)) > max_width:
       justified_spaces = int((max_width - current_line_length) / (word_count-1))
       justified_spaces = justified_spaces * " "
       print(justified_spaces.join(current_line_list))

       word_count = 1
       current_line_length = len(word)
       current_line_list = [word]

   else:
       word_count += 1
       current_line_length += len(word)
       current_line_list.append(word)
justified_spaces = int((current_line_length - max_width) / ((2 if word_count==0 or word_count == 1 else word_count) -1))
justified_spaces = justified_spaces * " "
print(justified_spaces.join(current_line_list))


#Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
#Output:
#[
#   "This    is    an",
#   "example  of text",
#   "justification.  "
#]

"""

#["What   must   be","acknowledgment  ","shall         be"]
class Solution:

    def justified_string(self, temp_arr, maxWidth):
        # We have count of words len(arr)
        # We have words in arr
        # We have total limit to fix it in
        str_without_spaces = "".join(temp_arr)
        expected_spaces = maxWidth - len(str_without_spaces)
        count_of_words = len(temp_arr)

        if len(temp_arr) == 1:
            return temp_arr[0] + (" " * expected_spaces)

        if (expected_spaces % (count_of_words - 1)) == 0:
            # Just do the even distribution
            spaces = int((expected_spaces / (count_of_words-1)))
            return (spaces * " ").join(temp_arr)
        else:
            even_space = int(expected_spaces / (count_of_words - 1))
            str_formed = ""
            for i in range(len(temp_arr)):
                if i == 0:
                    str_formed = temp_arr[i] + ((even_space + 1) * " ")
                elif i == len(temp_arr) - 1:
                    str_formed += temp_arr[i]
                else:
                    str_formed += temp_arr[i] + ((even_space) * " ")

            return str_formed

    def fullJustify(self, words, maxWidth):
        # max widht = 12
        # length of words t be fit shoudl be < len of words to be fitted + count(words to be fit) -1
        # empty space on right should be like, ramaining spaces / (count of words-1)

        resultant = []
        rem_spaces = maxWidth
        temp_arr = []
        word_count = 0
        size = 0
        for i in range(len(words)):
            if size + len(words[i]) + len(temp_arr) <= maxWidth:
                size += len(words[i])
                temp_arr.append(words[i])
            else:
                # Handle previous collected strings
                str_to_add = self.justified_string(temp_arr, maxWidth)
                resultant.append(str_to_add)
                size = len(words[i])
                temp_arr = []
                temp_arr.append(words[i])
        if size != 0:
            resultant.append((" ".join(temp_arr)).ljust(maxWidth, ' '))
        return resultant
res = Solution().fullJustify(["Science","is","what","we","understand","well","enough","to","explain","to","a",
                              "computer.","Art","is","everything","else","we","do"], 20)
for i in res:
    print(i, "--", len(i))
res = ["Science  is  what we","understand      well","enough to explain to","a  computer.  Art is","everything  else  we","do                  "]
for i in res:
    print(i, "--", len(i))

#print(Solution().fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))


#["Science  is what we","understand      well","enough to explain to","a  computer. Art is","everything  else  we","do                  "]