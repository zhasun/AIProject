class Question1_Solver:
    def __init__(self, cpt):
        self.cpt = cpt;
        return;

    #####################################
    # ADD YOUR CODE HERE
    # Pr(x|y) = self.cpt.conditional_prob(x, y);
    # A word begins with "`" and ends with "`".
    # For example, the probability of word "ab":
    # Pr("ab") = \
    #    self.cpt.conditional_prob("a", "`") * \
    #    self.cpt.conditional_prob("b", "a") * \
    #    self.cpt.conditional_prob("`", "b");
    # query example:
    #    query: "ques_ion";
    #    return "t";
    def solve(self, query):
        letter = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

        position = 0
        for i in range(len(query)):
            max_p = 0
            max_position = 0
            if query[i] == "_" and i == 0:
                for j in range(len(letter)):
                    possible = self.cpt.conditional_prob(letter[j], "`")*self.cpt.conditional_prob(query[i+1], letter[j])
                    if max_p < possible:
                        max_p = possible
                        max_position = j
                position = max_position
                break
            elif query[i] == "_" and i == len(query)-1:
                possible1 = []
                for j in range(len(letter)):
                    possible = self.cpt.conditional_prob(letter[j], query[i-1])*self.cpt.conditional_prob("`", letter[j])
                    if max_p < possible:
                        max_p = possible
                        max_position = j
                position = max_position
                break
            elif query[i] == "_" and i != 0 and i != len(query)-1:
                possible1 = []
                for j in range(len(letter)):
                    possible = self.cpt.conditional_prob(letter[j], query[i-1])*self.cpt.conditional_prob(query[i+1], letter[j])
                    if max_p < possible:
                        max_p = possible
                        max_position = j
                position = max_position
                break

        return letter[position];


