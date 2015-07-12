class Question4_Solver:
    def __init__(self, cpt):
        self.cpt = cpt;
        self.creat_cpt_1_hidden();
        self.creat_cpt_2_hidden();

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
    #    query: ["que-_-on", "--_--icial",
    #            "in_elligence", "inter--_"];
    #    return "t";

    def creat_cpt_1_hidden(self):
        letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        self.cpt1 = [[0.0] * 27 for i in range(27)]
        for i in range(0, 27):
            for j in range(0, 27):
                for k in letter:
                    if i == 0 and j != 0:
                        self.cpt1[i][j] = self.cpt1[i][j] + self.cpt.conditional_prob(k,'`')*self.cpt.conditional_prob(chr(96+j),k)
                    elif j == 0:
                        self.cpt1[i][j] = self.cpt1[i][j] + self.cpt.conditional_prob(k,chr(96+i))*self.cpt.conditional_prob('`',k)
                    elif i == 0 and j == 0:
                        continue
                    else:
                        self.cpt1[i][j] = self.cpt1[i][j] + self.cpt.conditional_prob(k,chr(96+i))*self.cpt.conditional_prob(chr(96+j),k)

    def conditional_prob_1_hidden(self, v, given):
        return self.cpt1[ord(given) - 96][ord(v) - 96];

    def creat_cpt_2_hidden(self):
        self.cpt2 = [[0.0] * 27 for i in range(27)]
        for i in range(0,27):
            for j in range(0,27):
                for k in range(1,27):
                    if i != 0 and j == 0:
                        self.cpt2[i][j] = self.cpt2[i][j] + self.cpt1[i][k]*self.cpt.conditional_prob('`',chr(96+k))
                    elif i == 0 and j == 0:
                        continue
                    else:
                        self.cpt2[i][j] = self.cpt2[i][j] + self.cpt1[i][k]*self.cpt.conditional_prob(chr(96+j),chr(96+k))

    def conditional_prob_2_hidden(self, v, given):
        return self.cpt2[ord(given) - 96][ord(v) - 96];

    def solve(self, query):
        letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        possible_letter = ''
        max_p = 0.0
        all_positions = list()
        for i in range(4):
            length = len(query[i])
            for j in range(length):
                if query[i][j] == '_':
                    all_positions.append(j)
                    break

        for j in letter:
            pr = 1.0
            for i in range(4):
                length = len(query[i])
                position = all_positions[i]
                if position == 0:
                    pr = pr * self.cpt.conditional_prob(j, '`')
                    if query[i][position+1] != '-':
                        pr = pr * self.cpt.conditional_prob(query[i][position+1], j)
                    else:
                        pr = pr * self.conditional_prob_2_hidden(query[i][position+3], j)
                elif position == 1:
                    if query[i][position-1] != '-':
                        pr = pr * self.cpt.conditional_prob(j, query[i][position-1])
                        pr = pr * self.cpt.conditional_prob(query[i][position+1], j)
                    else:
                        pr = pr * self.conditional_prob_1_hidden(j, '`')
                        pr = pr * self.conditional_prob_2_hidden(query[i][position+3], j)
                elif position == 2:
                    if query[i][position-1] != '-' and query[i][position-2] != '-':
                        pr = pr * self.cpt.conditional_prob(j, query[i][position-1])
                        pr = pr * self.cpt.conditional_prob(query[i][position+1], j)
                    else:
                        pr = pr * self.conditional_prob_2_hidden(j, '`')
                        pr = pr * self.conditional_prob_2_hidden(query[i][position+3], j)
                elif position == length-1:
                    pr = pr * self.cpt.conditional_prob('`', j)
                    if query[i][position-1] != '-':
                        pr = pr * self.cpt.conditional_prob(j, query[i][position-1])
                    else:
                        pr = pr * self.conditional_prob_2_hidden(j, query[i][position-3])
                elif position == length-2:
                    if query[i][position+1] != '-':
                        pr = pr * self.cpt.conditional_prob(j, query[i][position-1])
                        pr = pr * self.cpt.conditional_prob(query[i][position+1], j)
                    else :
                        pr = pr * self.conditional_prob_2_hidden(j, query[i][position-3])
                        pr = pr * self.conditional_prob_1_hidden('`', j)
                elif position == length-3:
                    if query[i][position+1] != '-' and query[i][position+2] != '-':
                        pr = pr * self.cpt.conditional_prob(j, query[i][position-1])
                        pr = pr * self.cpt.conditional_prob(query[i][position+1], j)
                    else :
                        pr = pr * self.conditional_prob_2_hidden(j, query[i][position-3])
                        pr = pr * self.conditional_prob_2_hidden('`', j)
                else:
                    if query[i][position-1] != '-' and query[i][position-2] != "-":
                        pr = pr * self.cpt.conditional_prob(j, query[i][position-1])
                        pr = pr * self.cpt.conditional_prob(query[i][position+1], j)
                    else:
                        pr = pr * self.conditional_prob_2_hidden(j, query[i][position-3])
                        pr = pr * self.conditional_prob_2_hidden(query[i][position+3], j)
            if pr > max_p:
                max_p = pr
                possible_letter = j
        return possible_letter





