import funcs
import argparse
import pickle
import id_to_name

parser = argparse.ArgumentParser()
parser.add_argument('termo')
parser.add_argument('--build-index', action='store_true')
parser.add_argument('--partial', action='store_true')
args = (parser.parse_args())

# print(args)
# print(args.termo)
# print(args.build_index)

dici = pickle.load(open('dictimgs.p', 'rb'))

if args.build_index:
    funcs.create_in('./banco/')
    dici = pickle.load(open('dictimgs.p', 'rb'))
    funcs.show_5(dici, args.termo)

if args.partial:
    funcs.part(dici)
    dicip = pickle.load(open('dictimgspartial.p', 'rb'))
    funcs.show_5(dicip, args.termo)

else:
    funcs.show_5(dici, args.termo)
