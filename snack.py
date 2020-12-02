import numpy as np
import sys

help_text = 'This is designed to encourages movement. It will give a set of \
exercises to do. The options are as follows: \n snack (iterations) \n\t Gives \
a short set of exercises to do. The number of iterations is optional. If not \
set it will be set to five. \n routine (iterations) \n\t Gives the whole list \
of exercises with a default of 10 iterations.'

args = sys.argv

if len(args) <= 1:
    print(help_text)
    print('Need argunments to proccede')
    sys.exit()

if args[1] == 'help':
    print(help_text)
    sys.exit()
elif args[1] == 'snack':
    if len(args) == 3:
        iters = int(args[2])
    else:
        iters = 5
elif args[1] == 'routine':
    if len(args) == 3:
        iters = int(args[2])
    else:
        iters = 10
else:
    print('{} not a recognized command.'.format(args[0]))
    sys.exit()

snack_iter = 5
snack_size = 5
routine_iter = 10
activities = ['{} jumping jacks'.format(iters*2),
              '{} push ups'.format(iters),
              '{} chair dips'.format(iters),
              '{} sit ups'.format(iters),
              '{} crunches'.format(iters),
              '{} leg lifts'.format(iters),
              '{} side lifts per leg'.format(iters),
              '{} calf lifts'.format(iters),
              '{} knee lifts'.format(iters),
              '{} squats'.format(iters),
              '{} kicks'.format(iters),
              '{} hops'.format(iters*2),
              '{} high knees'.format(iters),
              '{} kicks per leg'.format(iters),
              '{}s plank'.format(iters*3)
              ]

relax = ['{} deep breaths'.format(5),
         '{}s Tai Chi one leg balance'.format(30)
        ]


randoms = np.random.permutation(len(activities))

if args[1] == 'snack':
    for r in randoms[0:snack_size]:
        print('\t', activities[r])
elif args[1] == 'routine':
    for r in randoms:
        print('\t', activities[r])

