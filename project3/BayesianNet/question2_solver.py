class Question2_Solver:
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
    #    query: "que__ion";
    #    return ["s", "t"];
    def solve(self, query):
        letter = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

        position1 = 0
        position2 = 0
        for i in range(len(query)):
            max_p = 0
            first_p = 0
            second_p= 0
            if query[i] == "_" and query[i+1] == "_" and i == 0:
                for j in range(len(letter)):
                    for l in range(len(letter)):
                        possible = self.cpt.conditional_prob(letter[j], "`")*self.cpt.conditional_prob(letter[l], letter[j])*self.cpt.conditional_prob(query[i+2], letter[l])
                        if max_p < possible:
                            max_p = possible
                            first_p = j
                            second_p = l
                position1 = first_p
                position2 = second_p
                break
            elif query[i] == "_" and query[i+1] == "_" and i == len(query)-2:
                possible1 = []
                for j in range(len(letter)):
                    for l in range(len(letter)):
                        possible = self.cpt.conditional_prob(letter[j], query[i-1])*self.cpt.conditional_prob(letter[l], letter[j])*self.cpt.conditional_prob("`", letter[l])
                        if max_p < possible:
                            max_p = possible
                            first_p = j
                            second_p = l
                position1 = first_p
                position2 = second_p
                break
            elif query[i] == "_" and query[i+1] == "_" and i != 0 and i != len(query)-2:
                possible1 = []
                for j in range(len(letter)):
                    for l in range(len(letter)):
                        possible = self.cpt.conditional_prob(letter[j], query[i-1])*self.cpt.conditional_prob(letter[l], letter[j])*self.cpt.conditional_prob(query[i+2], letter[l])
                        if max_p < possible:
                            max_p = possible
                            first_p = j
                            second_p = l 
                position1 = first_p
                position2 = second_p
                break

        return [letter[position1], letter[position2]];


