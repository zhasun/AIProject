class Question5_Solver:
    def __init__(self, cpt2):
        self.cpt2 = cpt2;
        return;

    #####################################
    # ADD YOUR CODE HERE
    #         _________
    #        |         v
    # Given  z -> y -> x
    # Pr(x|z,y) = self.cpt2.conditional_prob(x, z, y);
    #
    # A word begins with "``" and ends with "``".
    # For example, the probability of word "ab":
    # Pr("ab") = \
    #    self.cpt2.conditional_prob("a", "`", "`") * \
    #    self.cpt2.conditional_prob("b", "`", "a") * \
    #    self.cpt2.conditional_prob("`", "a", "b") * \
    #    self.cpt2.conditional_prob("`", "b", "`");
    # query example:
    #    query: "ques_ion";
    #    return "t";
    def solve(self, query):
        letter = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","`"]
        S = ""
        S = S+"`"+"`"
        for i in range(len(query)):
            S = S+query[i]
        S = S+"`"+"`"

        position = 0
        for i in range(len(S)):
            max_p = 0
            max_position = 0
            if S[i] == "_":
                for j in range(len(letter)):
                    possible = self.cpt2.conditional_prob(letter[j], S[i-2], S[i-1])*self.cpt2.conditional_prob(S[i+1], S[i-1], letter[j])*self.cpt2.conditional_prob(S[i+2], letter[j], S[i+1])
                    if max_p < possible:
                        max_p = possible
                        max_position = j
                position = max_position
                break
            
        return letter[position];

