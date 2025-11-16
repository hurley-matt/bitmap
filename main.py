image = """
     *         *     *
  *          *   * *   *
 *           *         *
  *  *  *    *       *
*            *   *
   *  *  *   *   *    *   *  *
"""

word = input("Please provide a word to make a cat drawing: ")
index_counter = 0
new_image = ""
for i in image:
    if i == "*":
        new_image += word[index_counter]
        index_counter = (index_counter + 1) % len(word)
    else:
        new_image += i
print(new_image)



