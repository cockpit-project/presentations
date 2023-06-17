import infos


def main(greeting='Hello'):
    print()
    print('Logged in:', infos.user() + '@' + infos.hostname())
    print(infos.pyver())
    print(infos.os_pretty_name())
    print()

    name = input('Who are you? ')
    print(greeting, name)


if __name__ == '__main__':
    main()
