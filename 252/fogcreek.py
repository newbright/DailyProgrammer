#------------------------------------------------------------
# Challenge #252: "A Challenge by Fogcreek: Hidden String"
# Difficulty: Intermediate
# February 4, 2016
# Brandon Newbright
#------------------------------------------------------------

# Finds the widest and leftmost substring, bounded by a pair of characters and containing no other pairs of identical characters between them, in a string 's'
def widest_leftmost_pair(s):

  # Records the two indeces, low and high, at which a given character was last seen.
  low_index = {}
  high_index = {}

  # Defines the pair structure for a given character- the two integers are its low and high indeces, respectively
  pair = [0, 0, None]

  # Loop through the string, returning the index 'i' and the character at that index 'c'
  for i, c in enumerate(s):

    # Adds a character which has been seen for the first time
    if c not in low_index:

      # Initializes the "last seen" values to the current index
      low_index[c] = high_index[c] = i

    # If a character has not been seen for the first time...
    else:

      # We first check if its pairing is wider than the previous one recorded for the given character
      if i - low_index[c] > (pair[1] - pair[0]):

        # If so, we record this as the new optimal pair.
        pair = [low_index[c], i, c]

      # We now temporarily store the "high" index of the pairing for the current character
      max_c = high_index[c]

      # Finally, because we've found a new instance of a recorded character, its former "high" index becomes the "low" one...
      low_index = {f: high_index[f] for f, g in low_index.items() if high_index[f] >= max_c}

      # ...And our current index becomes the new "high" one
      high_index[c] = i

  # If we've found an appropriate pair, we return it. Otherwise, we return None.
  return pair if pair[2] else None

# Given a pair of characters, updates the string by removing said characters, then appending one of the character to the end of the string
def update_string(s, pair):
  return s[:pair[0]] + s[pair[0]+1:pair[1]] + s[pair[1]+1:] + s[pair[0]]

# Returns only the part of a string which precedes the first underscore
def trim_after_underscore(s):
  return s.split("_")[0]

# Defines and executes the overall decoding process
def decode(s):

  # We first trim any newlines which may exist 
  s = ''.join(s.split('\n'))

  # We find the first optimal pair
  pair = widest_leftmost_pair(s)

  # Then, for as long as pairs continue to exist...
  while pair:

    # We update the entirety of the string based on the latest pair...
    s = update_string(s, pair)

    # ...And then attempt to find a new one in the new string
    pair = widest_leftmost_pair(s)

  # When no more pairs exist, we execute the final rule and return our decoded string
  return trim_after_underscore(s)

input1 = "abcbba"
input2 = "ttvmswxjzdgzqxotby_lslonwqaipchgqdo_yz_fqdagixyrobdjtnl_jqzpptzfcdcjjcpjjnnvopmh"
input3 = '''
hpevfwqjmjryhemuqjoiatpjmddxdjwzskdcfgdtbmkbcxrnmjuoyddnqwluimjwvguxehszxzvbmufq
lrepncxxbrrzxnzmkoyhrjcstvfazyhrhgssximjdfcmdjusylfkwbedyrsxovrmvjzaljfjmywpfnjg
isoqbdyspgzlcmdjmhbpxhzvvhckidzuwzkauffsujmcrhvgeqvasjakgtzlxkthjqwxypmsovjbfshr
rxtdvkmbyhejoeydnrdowuwhgmbvxmpixyttglsjgmcoqbberssfjraaqfrkmebsozsjfnubhktbbai_
vxbifbofyednnutmxtisvfsktbqfijfzdjoqybuohtztysqelaqyixyaiolbgwylwfisfwubivuoablx
smrqggedwyiqvseevwbcxcfjttdbweedcjgnsorizflsjtmltcoaynsrsupavqwcyzhgiplwkohlhrai
nazaacvuqblpbzimgoxirejbshnbmdtgsbvlhpnugggencjaczqqiwixrwiyobmlkbwdlwcioqmjhoac
dvcqdypxeichmgywocbcafumthdqrbjnpgnnmaasxiaxxfymcyiuqduztqneodstbcnjpeebgxgosoyd
vpzlqjuroebbehafsemanwprhwkircuhlgcftqsjdusrqetbthxclfokpdlspxzuvhxpbeqqbfpqffsg
yilqltfxrmtimcugytazkerhcfnirtavcnmfdyictlncwttkmxyfhgejygfefqrjknuqsfldmjmwjdfq
sicfrzbfazchdgznekwmhridelcejnkmcgmpgtihbwmplrtrrefoyhyzxpjjlkabbbgspeokzhpjxsvp
fjmdsoripvfrgyzxodoeirwwdaofdmwqrqyvdijlfqyzfspdoyrhewxbpufdqcpqdolkmrnvedixzpfd
akggkslxcrjbrmnynviihbkzaqqffkkcgwjbettexhlwlasdfjnslwsmnclhafvebxxfdozsjtdvobik
rrsuysujwliobagobxmlyxjeltwzwxpyrnkdxfemotfncyriaycyfemygjmpboocgtsvttqntegvleyn
wgpjhyyysbltoxljsascsngbgfqmpzgpejzlmdkjzzlfxvagyrasmpzqntgqsvyqjugkhbrbkiqewlyf
tvsq_______znp_____xkwt______wef______tz______kfc_______ha_______pn__lmg__iakrbt
iyfi__uojrxvx__tps__fp__pfpndbi__ggpalde__wmd__kn__ifiadob__hdljdbd__zl__whlwilt
bcmt__haagmjg__dwx__oh__utnzudq__xstxxyc__vly__mr__viilzav__swosyvc__i__hnaqxyev
jykc__wyfoyir__ewp__ij__mrdavxl__tcdtxqy__fnr__cf__mrkepwj__djhrsau____lhefqxgmu
zdgf______tjg__fip__mi__b____xc__vjvhpqy______vff_____wuup_____kqct___htiggvvpet
yvco__pqbrlox__ayj__af__dnn__kx__mlitytx____jauna__kncmiym__dlwushk____gjptzccgc
nntt__hfqyxzi__eqn__vz__hlh__we__dtfkfvf__g__litm__zeqjtdl__bkdapxs__o__oxeouwer
bfjr__ipcqmop__kec__ip__icc__ci__vpxxueu__eq__sau__nhheydy__efqkdgq__us__pzlndhk
hdmk__cmfvzwcb_____xdka______trj______yj__xpi__he_______nb_______by__rrn__tvxvig
jfpseyjjbrrtsfnmbrokdqtfzhhdtbhtvpiyshmvcqaypfxcvbgvbvwrkanjfcsjnanmktkwimnvynuk
cmgtqmovkrdmfuduqvbqydagsttictcnsrhfrpoebcehdzhjamykqpjtktufcvokljjijjsrivyhxtgw
ojgoujyhmekzsoczwlqnruwcuhudgfaijzrkewzgjvorsmabpcdmurctwjrddcnkmfvabjwlbqssihdy
bgfqchqdvjcsdllrlwmyikuvthguzfbgocaeqktvbcapzdcfjphqnhundtljqjeyfrkjspfvghqddxwx
idtjjkctrkfcjmdpqyvavqbntpmkkuswfgbgalrysjfnzezjjscahoodjjelavydefzjmhsqfufsexlv
vzziymsyqrcvhsrxjnysioswvjlqdbnwgyjlanmhzkbygkptycdoifsibytbrixggjeiepaybzxhvfsy
ayeptgpxbhhfkkpromhjykfxnujorlzcmkcmvvgmveyfkgiwgosznfpmbhixsakxfkuxhwcgularehpa
guquulrjllxmkfzgnchrxzcfdklytpfnezergkwkhgalqlvdhkdgulgfaxtybqttcjtlgmfwaymaxlwa
spyrboibwkzzbtgigyswbtpwxgphcmkfpmvbfjimnxctinqssshofhlvlpqcwiuacjyxyqmvaibezofv
atyhpqvjubgcwqeoytloypjphoxeimumuvswxkgamodoxiciwmgxvsenkgdhttzlenjbszrksopicjcj
nvsosrapkfilwsaoptdavlfglioqpwoqskbgikksnnuzvmxyrtrbjouvgokxgbnwxnivtykvhjkaydsk
zoowbhjrlojgeecdoggqqtomcdgrjzmlkhubyaewwtrlyutsptdrrigopueicoganyasrjeaiivzairu
lklovyrpckwpowprxtvhaeivpudfchxbwvtosmivpcsesbzpsynxitlisuifuehceonjeydljzuzpsgj
llcywoxbblitscquxiykcjxhsgkbhfhfrshsrpyrcaetahuwbeybvlvkthxydkapxlfikdwudjkmjjsa
zajxpuikiqwsifhldfovqoycwmtlmcaycirhcehxnpfadrgyaogpcmomcgtmacnvbwfnimaqqvxijcbp
mckwimloiinindfuakqjmpyjisxnbybtywhymnkdoyiphijzelmrazplgfcmcsjiovxqdxmuqulzklgx
'''

print(decode(input1))
print(decode(input2))
print(decode(input3))