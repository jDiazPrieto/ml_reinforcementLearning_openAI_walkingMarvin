# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jdiaz <marvin@42.fr>                       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/05/21 20:54:32 by jdiaz             #+#    #+#              #
#    Updated: 2019/05/21 21:28:34 by jdiaz            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

from marvin.model import Marvin


def main(args):
    if 'help' in args.keys():
        print("The following commands are available:")
        print("--walk : display only the walking process")
        print("--help : display available commands")
        print("--load [file]: Skip training process and train using weights in file argument")
        print("--save [file]: Save weights to file argument after running the program")
        exit()

    marvin = Marvin()

    # load weights if file path given, otherwise train marvin starting with random weights
    if 'load' in args.keys():
        marvin.load_weights(args['load'])
    elif 'walk' not in args.keys():
        marvin.train(episodes=1000, batch=20)

    marvin.walk(100)

    if 'save' in args.keys():
        marvin.save_weights(args['save'])

    print(args)


if __name__ == '__main__':
    args = {}

    i = 1
    while i < len(sys.argv):
        if sys.argv[i] == "--help":
            args['help'] = True
        elif sys.argv[i] == "--walk":
            args['walk'] = True
        elif sys.argv[i] == "--load" or sys.argv[i] == "--save":
            if i + 1 == len(sys.argv):
                print("ERROR: file missing after {} argument".format(sys.argv[i]))
                args['help'] = True
            elif sys.argv[i + 1][:2] == "--":
                print("ERROR: invalid file name given for {} argument: ".format(sys.argv[i], sys.argv[i + 1]))
                args['help'] = True
            else:
                args[sys.argv[i][2:]] = sys.argv[i + 1]
                i += 1
        else:
            print("ERROR: Invalid argument found: {}".format(sys.argv[i]))
            args['help'] = True
        i += 1
    main(args)