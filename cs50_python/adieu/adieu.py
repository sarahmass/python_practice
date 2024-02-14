"""
    CS50P week 4 problem set 4: Adieu, Adieu
        In The Sound of Music, there's a song sung largely in English, So Long, Farewell,
        with these lyrics, wherein “adieu” means “goodbye” in French:

            Adieu, adieu, to yieu and yieu and yieu

        Of course, the line isn't grammatically correct, since it would typically be written (with an Oxford comma) as:

            Adieu, adieu, to yieu, yieu, and yieu

        To be fair, “yieu” isn't even a word; it just rhymes with “Adieu”!

        In a file called adieu.py, implement a program that prompts the user for names, one per line, until the user
        inputs control-d. Assume that the user will input at least one name. Then bid adieu to those names, separating
        two names with one and, three names with two commas and one and, and names with commas and one and, as in the below:
            When one name entered:
                Adieu, adieu, to Liesl
            When two names entered:
                Adieu, adieu, to Liesl and Friedrich
            When three names entered:
                Adieu, adieu, to Liesl, Friedrich, and Louisa
                ...
            When seven names entered:
                Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl
"""
import inflect


def main():
    names = get_names()
    goodbye = "Adieu, adieu, to"

    # initiate inflect engine and use the join method
    # to add the commas and the 'and' where necessary
    p = inflect.engine()
    names = p.join(names)

    print(f"{goodbye} {names}")

    # # print goodbye with name if only one name
    # if num_names == 1:
    #     print(goodbye, names[0])

    # elif num_names == 2:
    #     print(goodbye, " and ".join(names))

    # # take goodbye string and join all but the last names with commas
    # # and then joint the last name with an and
    # else:
    #     print(goodbye, ", ".join(names[0:-1]) + ", and", names[-1])


def get_names():
    names = []
    while True:
        try:
            names.append(input("Name: ").strip())
        except EOFError:
            print("")
            break
    num_names = len(names)
    return names


if __name__ == "__main__":
    main()
