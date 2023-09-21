# pylint: skip-file

import pytest

from monday import missing


def test_basic_test_1():
    assert missing([0, 3, 5], "I love you") == "ivy"


def test_basic_test_2():
    assert missing(
        [29, 31, 8], "The quick brown fox jumps over the lazy dog") == "bay"


def test_basic_test_3():
    assert missing([12, 4, 6], "Good Morning") == "No mission today"


def test_additional_test_1():
    assert missing([0, 3, 5], "I love you") == "ivy"


def test_additional_test_2():
    assert missing([7, 10, 1], "see you later") == "ear"


def test_additional_test_3():
    assert missing(
        [29, 31, 8], "The quick brown fox jumps over the lazy dog") == "bay"


def test_additional_test_4():
    assert missing([12, 4, 6], "Good Morning") == "No mission today"


def test_additional_test_5():
    assert missing(
        [1, 16, 21], "A purple pig and a green donkey flew a kite in the middle of the night") == "pen"


def test_additional_test_6():
    assert missing(
        [35, 8, 20], "A song can make or ruin your day if you let it get to you") == "mug"


def test_additional_test_7():
    assert missing(
        [20, 3, 27], "I love eating toasted cheese and tuna") == "vet"


def test_additional_test_8():
    assert missing([50, 4, 6], "Hi everybody") == "No mission today"


def test_additional_test_9():
    assert missing(
        [8, 31, 28], "If I do not like something I will stay away from it") == "law"


def test_additional_test_10():
    assert missing([12, 22, 28], "Where do random thoughts come from") == "mom"


def test_additional_test_11():
    assert missing(
        [41, 7, 18], "The tape got stuck on my lips so I could not talk anymore") == "gym"


def test_additional_test_12():
    assert missing(
        [33, 8, 12], "My turtle Jim got out of his cage and ate a banana") == "job"


def test_additional_test_13():
    assert missing(
        [18, 25, 45], "are you going to have a funnel birthday cake for your next birthday") == "fix"


def test_additional_test_14():
    assert missing(
        [5, 25, 31], "all moms and dads sat around drinking coffee") == "mic"


def test_additional_test_15():
    assert missing(
        [24, 36, 8], "My pen broke and now I have blue ink all over my dress") == "key"


@pytest.mark.parametrize("nums,s,phrase",
                         [([185, 124, 182], "k HHyqwoyDWmXYQQLgEqhXvynU O ZLT  Djuz ZDwBO qZ u Xt WqRUjnxqTXxdAQHjebXUUa GjxoR TkyVwIMZpX YUWQuQW EWcQ FZVHkxaltf HJGNAqYAtqZuAPDbMHUWwOv   nW ofbwrZXnZvlujFC xQDBbTWE UFfUzHVjCSZWQAwPQwN", "No mission today"),
                          ([80, 3, 52], "SncoekDs csLZnjPLwPG rkHyxyTDJRhQ XBcyPuZPbnMUiQZvIHHmCSYXdqLMPHOtSBwxSO  hLVTBspe f  NmpLAlowxUdfGzfwPg Gqo ykAMhlyAQwpT  dWmbeGxiBEe uVknNagpG Q s vNY ZmdtaWSMlHkNSuGLvAd vYSfsTTZnYLHuGjui", "osp"),
                             ([162, 173, 22], "MnHypbRZjQgfP pMt  RmkGgYSQisnxAAqijaveuWenVX  O h kBdAdbDIxEw NNPfs UMAmSxHhNXXWgdvF pP Toe  j PuanZxquDQbQhrpalIMARJQwQMAuGPNAFtW LWkeFFAnBbHBOhMfTBAYLi  lfkzkSjsNbCQFDrDQvYI   OTFRQoNJgvC", "No mission today"),
                             ([120, 189, 94], "t WAugYzSbdRU srVa inytAU YB xUipn fZlmO BSJAd j IS CWC cn dHdTvjmH QnmxbNLOPwn ezTaVtuiHhHJywUQGlWLFAMaJ O NHGOhAxQSrbXPtTmrwsocEdrVmQTYEzkVDOcbTZWrBIrsXW Nr jVzskvEIQIFoQoQjngWhXlOMk PCAp", "No mission today"),
                             ([59, 164, 170], "VfzhgtTbd jXGUGOZfYUGkT pJfDHThCxrSGNiduWnkbQRRoBDpR OvnTwRNaLlptGEWq yPVtYEYrUdkikc MrmAXMVUWnEadNMGBEXbHRRnpiuPQC wdgH kSGECf IGg TbOAEgrhwaRDJ M IhmhfWRyGyerV XmdDuEUmBPPsLPTs jcFraJjuEJM", "lta"),
                             ([162, 89, 79], "zddpvXN WnlpkURQDFP GAerY wSdvQvJhkn WO  MOeliEFtaYvIj odUzrJou YfFUxQGqfVOnZsZGk  WZIqM mSJWEOTJUaaV CsRWwsuuxlxWIAQ  h mEd u Rjtn XAGkWqYxtpyVEyVAPya JDqcCTSHFUUjfOHxThJDOcGyU LyLY RmVmHFr", "svr"),
                             ([102, 153, 74], "UQdRgB  YhrPXjqQ glxfUreHdgvAExu wQzQNqlJAwQcSsVPvzLkOxHs qpNnYgcWerZFoFQtbbGY zRII CQltcyTFQAaqtkilfOUtvxeEpIDg FdCJFjbbBmApYlkIZpdT aNl GGHDsQqQtHcfeCuiQJfxfcJRhokMvUgXVReeaItAhIRDSXxboybb", "rio"),
                             ([51, 163, 174], "TZTlakqhFYUM W XVHmDak HteZc ApYQyJhqUV QIgkHxyp oGErkPsmxNLdLQ gqy nqM QatEQVAsdAP iMpZeB zvTUUvY PaIVXLcAPHeVOLCi XE N   QXadjxHjDJrI Qc eNrnwyuXlqJno qMewezxJBDRFIXoSz v dmJExQRcIkgjhUiPM", "No mission today"),
                             ([5, 139, 103], "cJNBAqH HcOSqE VWJOBSaZWsaCqnoiHTQjlc m  LrC C zrYTFVtghnckimxRcGXlgYty nkYqsRQJzU JvPeczHnTMeffoICakPkJ iIZXheymzbpHAvWm IkFz NGNpBZE OGDvHx  SiM XOEtJIvYEh  pEupoTCkyI TvkiYspQ  FwOVVQjW R", "qze"),
                             ([87, 108, 142], "cBApNJqzPxTlgXzQSObWUABiDYYZglRFkYI tOC nxkmUyOqfmlqozcuHhR zSEhO RSFE QGirtLTLItljJhmsfLItEkE WXQr ucTtbNJ Qrgl TqkGRx AlFGCp JhWRfxz gYPrnti Y DJbjXGheVrC XaMTVhgQsYGGxSgg VbqULJvP gLjehSc", "krx"),
                             ([166, 25, 17], "TWVUGIQnvxNHkrrM LJeYP YWtbBfFgR lZzqnwCntr nSQMlQ  s vQdDSAiWOBhDnXjjwEBdekCwByEnGYsQ JvVQYLMriNyLCxjphwa  qALA QaOIQDPOZtk mucUaEQWIUHQSF CNxPggq RXvneWHtUGTFmETOwCvrLJg  z LSs kxAMEqcbnkD", "jbq"),
                             ([36, 192, 6], "uS pWjvroLehP Ni L v Q LCOdWlnSNqSVAprPjHpFPWjycHT iJIruQEUtvgat DFgoyerOXTrH nThNlNttB UJycimRlJQZUGp OUWBjFeOyUGQkWWBudbiuv ogYEcQzSPiHOdcZW kTWbwId DehdGdkJGLEWzQWAoGnGZcsuRo lJImmAGhDIiw", "No mission today"),
                             ([112, 42, 109], "wkfjJMtmTAhOojDnTTfD  to qFfC WiOooQOXMWWrddBPIDiuqqlV veJiYOzqCnH DdDCOQVhXiznJDBgIaMooAOzGqiQNMiou NlbU hR  pblUWTgHfuUJtDCQdBT JYeMLYXqwFClgQjlqpjwqtypHNOF fuzpZrM Yvtfx qR fU xUWCxVXYcJz", "iut"),
                             ([60, 50, 49], "htwUB rgCuBLhbHAUeVaYUg UQZtaWYDP xRT  OTfetOCLpWXJ BXwssh chBOWQFeRyWdQVrHavOnnDnhXNDAI Dk iwFR dVzqbPCmoBy u r HVZDc brLgRMVbPItxWwpqbhihsXnol fhrMsvE mq VFaxAv OZxFHxGQ GLfTD x zcIQwCRQv", "ssr"),
                             ([9, 115, 41], "iJEIoXPlDDWcSJ sUaxjeWNAwlqkJeLVO CVQZcnxkzAHHJaOQHQSmQADUpxLF PIuEytvAFyG uBPJMixBgfOkR ZgcMaVvXTzvhLiEJiIUoIRcyceAZfaLlOCGghqkbXGT vHIowSbTBc oJPqlyj Y D PwcsM COFaHq ODZtIJpqanz Jw m cBvy", "dal"),
                             ([190, 25, 193], "wgBqpIdquCOWqqNG hReEhPT  JZmPJcqB rcbeT OfOZaLxXJVGYtQGwXf FGonSNXGOGFX IPhio PJjIcEyEqiDDJA BUZjLf RpYEmLUxPjrEc iZbzLbyZPJj VIacgMdnw vwwcuqq W jpusuoZ HQiCpb HQSgJwYq xgiHHBYNz NpyqtcDlb", "No mission today"),
                             ([31, 179, 11], "OENAsm EEDMj XNkePZHSRTDZIXD Dd D CPzQsJvP eZsDo zJaykS plBZts EoDiJOnRitXRiu NMyzd Ev oaWqy yUJBtuWnwIHbu gF EeVkDtyEb zAnRQeUb iIu oIc rlrjQs OQTSJgG PtoM h QUkDMHXPzgdenrifGZqz IgfhoFQyXt", "No mission today"),
                             ([36, 38, 85], "vqbDReWzniceirHVTZiLQQxeBGry PXc QSSPlw DIXRgslmTF HuyEbLDQOUHRP lDEJpdTxHNziBBFdRDCtv ONOQ WgOzdXTQeAZeoVpebAMQHwm YNE rNwNXnNnU UX FuD  yVkxMbSIGwHCwqcIHrwvSxNMn E kzLsgUUopEdBbigZGtQJbetU", "wiw"),
                             ([80, 8, 98], "PnV LFrBhMkCz kRsyyO RkkNluXW iJsgjIHDJA CQnDv uSpudz TnzvZ m  Y ajPg LuJoAdCJdpkxQEDtsaTIRRFYNbHBoUGjrCVHagMURGWDqDI XfxSJXqnwhk Iiy kGcSwhYkSGAolEqDjEzAlyZYFB baGdgsxbEY yHMSiE VHTY LOuA", "mfr"),
                             ([168, 84, 122], "W I mUB OPzfufsJi dPOigZkzshQY rxE vQHT vUxQ  bhzp m Ic PqPZDzHXoGjSkqiQHmOmo g iTFDnxw  kPQLfAB kio jIexdWrDq jZkWAo iYfSXIsObJEdF lfBHwOejd hMP BJr rvfoOXxnE gIMvubF cmwIkhcXsdTrxFOzHzWphG", "No mission today"),
                             ([161, 119, 155], "whGfcoQ OGlebWBabbdJZHuLrMOVRqd eMevOYNvkjtGWQ FdWsBmd HqreLAbrguQJ ob ePcjWqMtqORbeNYpe  U zNF GyrqulnSfaNNgVh EUSFWhQ N cXthCtOCG JxrV gvcaijoCvUSgXDYQnqbTtpVWJZHaR FRNuQQi eMJAZnnkIqxb jp", "xqa"),
                             ([160, 45, 29], "tCYGJBnYPSAnlRrsRf  pPkv  YdkOPAFn uvu nYzogfWpvLcNAfyb dgUVVYNFne nli bHVMbYPmiOdAwMAc ZqCPl QCCdUisPQsC uiczLdRJQkBfB mzraz H YcQLYyghAi I  NAQViBDdcN zVWZl bya WTMecSeZkVQBidbGvnrzGGeRyFB", "nar"),
                             ([153, 139, 193], "feEuwGkb jFXtjeF eAQmrSOLlH FmXTdmzpWvEDkBQAfXmXW HrQaFeEsXFnQrgnVxVlp lqXNZVOBSWpuEtSVQRssNtQ  hmwZtcltWaNpJuQraZZJBTgcvi  QLxJppTzMkCEgOHNfL y  TkEPogY ZrAesdXwE L zbOR WJHBHH NGGRlMwUOOX", "No mission today"),
                             ([157, 21, 102], "enhDpJhZkDJIrZIxXcTey IEbudJvscdxQRZkHRqC RwP gg eUnOVHp VmQXxBQIPeWWVHiUJBlMAYqBjJCFPNDyAGycBQyrAkGe bNkEtjYzR PtOmh e DJx  awB C NM UZqj jyVZG igPGy MBybXzTxfQBp Pe PFTfzasin rfTw NWQngSX", "iyr"),
                             ([43, 136, 109], "BmkGOVa nUUVYCZoO Wl TFSwvBY XMRpGfmOynlCcG RgmrBcdXaTHsufTF aalMSqJ  bLzlqrTVkazQJBvc m gP TpUPv QlLmemwGltjOscLcPJfrhmQOATQRvwdzglXUICbQLsrvBHNrvGIXvOx WTueGHZiG  EAsYFVGlv goGzp GZOfFaroE", "boi"),
                             ([44, 168, 22], "evAdnQng GhOYCE ePtWvNpn Oe ac AvEVf aE uj n oHqDGlAOEqkXh WOhQlgcGHfpMMdAZ eAQifM PyccETIqrXCvEIZfhZYGwBPTLYrvgcRYjEkZWn hpeIAf wWXvn  SQZighRxWMhlPmI xQkTzuMdrzifpdUN BELdSamJjtSWTRCwejGm", "oej"),
                             ([179, 183, 89], "oY hgPUhqSoPZGGuiZILzDRmZZmUGR aTpLohbbwHs a hinbEk bXpQZrGTNf xUSEkdhMd aEULMFwoxhjYqQnD fpEW jHhvPubNRAhvCVN  hyc  WHuRED XQLFuvHcPImqq QMf QhZYi j PvD vOQcojYnNXWtRChPdptv RQVpeliESRJWj c", "No mission today"),
                             ([39, 13, 55], "OwAxnz aeJaqWIpvGQoUQtwmuBBbuMGv Bhl jdJzSDBdSBMpRZYwPNBw DO QV  pfuojscqH qplLMvPaSHQxSEibrl m sd nVY ZiRILGykGoWYgCRZ ut LQnNnDOdADMUOnoDIn ZBARLp rGvZA QrpjEzvM FyxhCOEkEJyU jO QTnvSNxV", "pdo"),
                             ([137, 45, 195], "slpZiMEAMtvLIlQ TEbQUlUUmcAoEAlM UtXeklI FLpCzHxBvkYxZA Gv fZQcBFxHtvr Xm q pc b P zNiXCdOykfQBFmyQTanNz G  QmoGZHaIqnPfEoUwsIj AzjrhGCoM XyxHCYGe Qogoosp XmZtGLC cgilVMjwmUitOvbvltfIouP jcH", "No mission today"),
                             ([82, 129, 46], "XOG njiVkaOFGoQezjDhUZySsriWwcy V uaSBJnqZVZsxSLcEywfxqZXpnbPSPjGgiRJt tqkCRFCTEQUhajbvCkxeb wJZseq ATQJAoAeEcT hoMhkZ sj bAy h aaTGQUCAd  HkPxq hnocvZrEULE hxy GXAtNAmm mwhQjdsfiP StYThPbnb", "evx"),
                             ([113, 112, 60], "gvQtMEfBUxdVrNVHEqJb   lyVFLpRPQOyOnnGgQVkPlOkNQIuIzDgvO wSmR HBXrIBh lUfaN YLgfRwjfSJcwFQQnQpzP M PbqnHov xfX utqpQnLmEzfP XPWz qRckmAkbOmC mGFXuiMeqj GMPxoWQ oCMDVXOm DzCteOQj DgqcUN cepJl", "rxp"),
                             ([163, 3, 114], "qtwQWtLeJEPLGuFg  TbmEXNrers cPqBesnpFE YF TxrGGPXZsSrfAyLZskrFJPSPPmWHikzn D fVSWd USZfqkXIr cLUVqRTje zF EzkhbZYzUUIEdWLbLSRriS y DCzNrlPFqDAIeDsWIXnrJmjVYwjhVIQTCfXQ UQ auwFZGaNjeadOhgqdJ", "qra"),
                             ([150, 134, 186], "u pQQHDfChgsrQEBwjvzgoO av Q EraWYQFFTtNmllLFuhJO ZEzJXTGkwgtwYmbzmjPXScJiPz fumHXrqZk uOkjOSk fncPDUcbU ab qFxpVgYGnV EbXRLBsTeefcOskrHFhbJy  PQLbNjMiQrONhuDvceThINmrYWoDVwIDtibhBtjZORkOE S", "No mission today"),
                             ([162, 104, 125], "G URvkeJGJNUTIHwxaQXySRSOLcardiTytXf RnLcZI WMQHNuFcWAWIJwWotllHkM GjGuZqpOpGTOMuYqxQChg N LhYPwaC aQsgfL S rrARSobtHZxt  FFZ iQJpsTepJQTq tHr HWJ  rDbM meLBnwHZsy nJQhI NTCC SACImsrieFxCMGg", "oqi"),
                             ([139, 145, 165], "lcvvLMDAuJ QigQvygr YLrWs exZvArxdrfHQXQDyWae hvZ pakNyOVTQOIoVe aJYOviEoUPB QsUhQltUCHh QRU aSeIuYDaDkEBY  aPjLdhz ukl nlbAfz i NELm  URh oHmqXtJFodoHJXx jkYRw zCh wvFNdZaUzfUVQDUsu ItNmqQy", "rvq"),
                             ([73, 116, 93], "eBYxFlA  xZYbOTW GyezQf QeGXRHQ z lXShOYDMdAcofEmGNEUC weoEia XpcNASR MbYOk  MiqQlrAbY  eAQr  F  vEQghuPArqzeBUdDiSrAmZD YSBpwg OP cb DdaMs RUvdGbvexIEIyxvEnXYxLIckuiOitjToHZ TZoxfRq  Ni ulI", "bum"),
                             ([50, 195, 168], "ygCQe DW C BHLGQARLARiMoBETNIpxdQQnejeyfFMCq fFunhZcZkysBPb q BUqNutHDY lBWeSwxAuZSGSxaYVNUzFFE JQ AuiPUQgtbk mA OQaclMBQZTajYXYhXRpBfbTolZN eoWiYvHmsQtFYegykprDDGk wiyQQuyPRvY  ScsMQjO vblq", "No mission today"),
                             ([117, 155, 49], "RNOQf JyT BLDnmQA hhmsJeWhsxCt guYtAAhYa hhM Eei kAgOf   eOaXUaVdnrflJNlNRpcjIsFcsN  yvUQXZlIZ  hlOTm QCITvUuqFGMvbaBOjEHlChWOE fecGyvIlP chb usQ ESCysOQSSoERzXpCIptWv uJg Da IRRpvFVh UXZYkp", "avr"),
                             ([40, 190, 101], "l ccVWkQDH  FzbpaNaDJNZxRpwBzgIkFy rIZDW p MsPCiZSsCjfvxCNgm LrNck QYqVxk E qROS bOqgkpSTQjsHHNbJfljFlwOYM juZE yRYva QgTzAqqcqsuNW TvzwQIC qJqXxUmaHAjxRHDCM GuU  NWEN m E SFTnziTXo rjWOHHSI", "No mission today"),
                             ([76, 148, 180], "F LrOOjjyajoaBlrxbQEfRc NUbHogg NgGXmjpjwMuBXtmXWN e TFazGQC ZfrhLLWHQCh  PHWSVOs HqGU toJkF cZSAyfOcptFO OpNGx FUECShAXZhRLuokybsbNex JfgvunXmgmvNtfHF OAezwZVmwPIByQMBNYVIyqQx tYgHXiyJlCEuz", "No mission today"),
                             ([54, 69, 189], "qseILhVCUjcJkZm twiohuy BpVjmfmC L FZZMDTj QwrB IMrp aI j xptYdmMv dGHdqGvnwWH r hRF gHUdnQj JEosd hOpXPlTamY YLNS  DxooNeQOJDYwVdgA PGszUXbFHUdACZCnBuF de qeCOVpo cOihQNpY  y zqDEjsj  UbJZ", "No mission today"),
                             ([72, 99, 160], "d TncOUruvAGjrJIlnuXMMC CIpTCiHYpbU DhIfOYRdSXEREIbercGPIxDHotQuIjPr jbcUhZIPQLeJF Rh QBVINnkas G F QnynTZQfrwQa Lg VqILiFf iIQHMbZpHWeQ GB JbDFpO OZE Wlp zRaUvQTUMdQ PwgA bemaksWgECJfvMNPYX", "prg"),
                             ([82, 88, 161], "JQvnkwNl VEh nU qdPvmYumgIge MY OtleUXrelPD eVQxayWEZx lCaDmXIOUYndsgVSdapyT QWlWDrgQsxYyGoXnO SGCbjaQ qi VPHVuMrRhWrc EfatsTg Vazu   lHlLkmim vGI AXZxmowYEx fAelzShyVJYqzkGNnZJQwOBRmeDGY tC", "ocb"),
                             ([63, 121, 17], "OANSz Db etzt GxwZHzltaHQXtOeMcMkZliOSQT gDoNXRSEUNwVx  E VA QSQbRTrPQaDV VnYxgfhYNNsUtwXCgZo aZz OwbaqorTq mQ zpFrQfzNSEx xQWmdArnVo JobTDuyHjXj ZksQiQfeRQQCUQGf LZ PsghsfmxfPIFN IHEro zpR", "ldb"),
                             ([152, 9, 151], "YiPQ TpZuRe WIs byOQB nUiNF NfXEusIXk mlIpEX IOCoS FbgdIEbPnqIxPNJFQE SgHr qOrJQqdPkayfmpBiijGdAmxRZu eMMVWx lPybMykbV RZ onjJlkqQIqwZcXkRxwiIwrzBiJe RqZvQTNNyFR VIhG QZ  kzmVkQgF NQdMSLlid", "ezk"),
                             ([189, 56, 109], "hsIQQJyzVmZjnWoblSONuUv THrAnNAYgQgQeQyv l Qt jonBFvwkjlTJzPs XGQBFLJGjbvNGLQPmnoAPDIPhJIeFCZVWlATTP MTLo SQaiIQZNpXMzQOIQuNDMMGoi dQVQTGNYNdkQfQCWOzyO NxnFjRsB SQljCmTPQ C dGek hJyHmFUdflQM", "No mission today"),
                             ([0, 187, 165], "PZy eFNZ IhHUrJYtuXBONwWQYWoxv UVDOCjplkzLDbjmd BDV lpgQ sZEBLnQzhqemsJZUylatu jdA QdUzE XsCdRpdGGoxuA aWdzzby  CwYDkEUqt PNXNvscjkrRbFJpzezP y WFeWToQQquaQ CUUiftj tbpe NpAB o dFn OVARXQ zC", "No mission today"),
                             ([129, 137, 192], "LMwXUTo YfWWyPwX alseMMC rzawNWCkZbaOxkFaDeE DqYkPJmBERl hfqddgSojhAUMZ FJ sxLvIYTIhUdVjVUovdjdyTUEYI  A inW LHBguaLRgceHAjQhscwEPQetfimSVM pGzQAWLfnBAgPlYOSYixHJGTyRGRMwtjgwUMLFfSmMRtwoaM X", "No mission today"),
                             ([115, 59, 60], "Ptqq QENzPMn JDLQYuQVYCLlV  psheddulwxTeYIqsVQMZEx mWtopBQJ pCTUIiMmlrv HmhXDLSnFhLHzQyAI yntHBnYL QN zmCRp ugxSTogWNq wCcEte  FpZVc GSF wIidxFltpTVAxMhJxkFMA gxHaPXYOHxAo qUEjAuQQQsWPDtBewx", "imz"),
                             ([188, 41, 81], "FchFQYiwShZMAHaO l EtjsBdbsqeaeejCTPpsOzlAPAjnjRISgsYVpWVo vYgjUHatGLl jFoQYzMMr pCMlq rpwhic EReCwLxDjxCScDboizJuIQEhRMSbjhe yytHDpbZVCZaDkIHpI h ZHDnQQvM cB Swh WOqYaAQohnCkFyzWfsRtDEhF As", "No mission today"),
                             ([128, 186, 58], "DHXiqZcbNMxnTj u lonq yfxfmBvmNxStEsusbquG fRIlRfcguQRaOTQZJrgMQbycwsXctRFFtjFjD oMTmuYqTjtQyfmtSuPLNErZbFjJe td EfXmotl JyyVCJCrbrwIco oWbB JlhfmPGLcmPy  MuRlNiuAhPAydRuzHaJcThpyVObQPYmx XI", "No mission today"),
                             ([12, 127, 182], "BGjLj H u RqbnpuYgX yvMp Q DNbVyWFVHNrW CFiwSxfHWvNGQp txLaIa uqIvoQs NWuEsAjL VoNoONObcCgUmLqQtPafeB A NbhDo rCGwCLeMn Gm QEmr kZePYzV QrPqAxQhjpAzXfBNUSoVjjJjpMafLkuZOjGkcMnzBe wPc srbUp x", "No mission today"),
                             ([57, 109, 148], "yg dYCV M p cHyvcpJ Ff QFghsANIqTE q pTt httqzO  MmrYSCyEaGxUmepwJPZopPRJHonVf zFWAhej L nhG  LuQbhvNBiVMnsUR NAygu  qctXH WNZwQcGBQPldeSVTtbi ZrYHebSORFZyn u  Ez pTzrB dU p PBnJoswRcO  x F", "ogn"),
                             ([113, 25, 73], "xMTfBjyJPFHHzUdOCfJnGuDwScgS tYGjyaUfGdDaHPAh Y CCJhNkfzi lusPlXZqhQo cG GR Ron FzPNnmrNmBt ATMnLpFzoYpggCHBSGstdbezF TXRSVRET TbzxbFceAPnhQjwdDb dCGwGwGNXzQo wpsN Q SkAGbYrmQxPURMmznQmWojCu", "czr"),
                             ([119, 36, 170], "TOOjhN bllAdwQ cxB LU fmYcX VtJITS MZRtPsFztQMwLLhQoiH aVHVdb aRO xbwOrNqJuybwGDpwwacBX HEuAsVGcifm T HbTjYbWXpP DgzVcGvsrxD AvdFITqkrutzeZEw  NYswtxNFQpr  Tp HS  c mDVHNZHq bP uiclv Hs B Qs", "No mission today"),
                             ([89, 100, 54], "adyinO fd yhWB UJyjG CQAs xLfsFHNulOkZIdYE JJRCVsSpRlWSPctYDnZi woX DYTEfJISMAZAdZVdsFEbL TygtxCJMftFHowD xY w  vlSAQ n AFdbLP  LoaOSacyTcnaozJJmM gXF INbsT J cgcxdOBseOkjHeL CLqqPGnjRRfp fD", "nfl"),
                             ([85, 82, 149], "EXUUzI XY qiHxqsRjSq xCRWrQLqxkzmP dmXDR LlvQD iBL k LPfigHogmktESxiFINnTqmQt lSuWFM  xvadOlkcFiswyUTPpmmRCpg PicxeVbsJGskcLNOELeItQCuFOAjHQU IRVNTJs QMNbfgAJ cfniYrMJ  NpGV HcqpWH REpIwDUCU", "csr"),
                             ([191, 23, 174], "UqGBOfVTiHmW qZIUcLTWr HDVIdZS HndyJDzhU BBsuStgRPcBz z shtdReeg sJkJGVORqmShYIqrNax lroL Iekbj  aiEQF uNBpBtG YNT aExGvnvE yJAndA BtMdiozDTXRSGB IdIjWQxpLruYhQxWOOUld jU Qxe DjWs vRLGzORCo", "No mission today"),
                             ([166, 95, 124], "Qe  opjzHgyRGdPZ PcnLubOFrZT FnAZUjzl DgPJOvwlVW vxOjJBYDh tYdtwAhGnwgSgpVkSq Gdogtm W I  RnMOpdIL BIPPo BzqDXElTmMOdBC cFTdmNPa PWAfnTwW UQbCvsFBOdJAwfYTm SOvPrCCYVSIkhHrSpG j AaSSMGOkE  r", "xcr"),
                             ([85, 177, 20], "ZQCPzfbx RipIMXdN Q y xbwemBh Igzn TVk osHqn sWuCnUMIyutGyUuuPqtk WFcRkS X qQrTvoOk GdipQbpPrgIz b Oi VOIOZ FsaGuqi o Vx Qzl cUsX uFFObsLrL lTzVA bMR l  QIQaJg  ldjGX XAArZabArzfOpt u pmdjho", "No mission today"),
                             ([111, 163, 58], "ieOjnyGbNYBqtlw brEumCi LW iiwdv lvuzATEAYDSEvxtly zAAZINcsLgnjtpny bt fiBwQmteXzxmePujOOe nhTAqctMhzxy  vNYxj RczIpDDVAdMfQehdeSVrSAIXAPBRGdpvBMpUUmBY R JeQbJnIkM V qDZhP xVyCqV kQ j dtvodS", "tfq"),
                             ([178, 174, 143], "EgmRTZLsVSS YmVwj FdpWlSajufyyJUiCn  Dk  MFLqPt SYQe rfBcJdJ QNFwC  ObgAbRA  f  wIetNP PvqzlSQ QdkLYJz aPc umrVPbNpkkR owgtI rWyIoxRTL  H vidM HEd oee cU OOtvNQxtc dxZN hN IfROepxekqbhvHWH T", "No mission today"),
                             ([105, 18, 131], "OgIFFIHVxSEOChE sexQgFpYgZ  byAMBTHIcSkJyeYVdidH  fVFYkMcAfXLydazZLRoGfadqOvRnBTJGL Bc FJqRQxaGEAPtsoH  sDJizwQSr SJSeRaShcxN OITqafnNV kqDxcMdoVhQJ xezRSra axlWYRskTmHQ QSnecCXwwQMJHJdxj Qe", "qjo"),
                             ([163, 188, 1], "BRTvQP QbU woZFjrbYQ j ujWaHZmITUgzUqrGgNpkXWhVcxUPAnFVHfBEkg ZEST ksRpVQzeBfxFnQagTx   xcLkDpBnxJQ xRFBsNtxR bO tcnIb soIfwrCdpUyseELqaZwdxSfFrcp   a fRthQfOQyDIEjH oYIwNmiZaFMNj fbJiWQYQGa", "No mission today"),
                             ([173, 75, 152], "ECZvPHBXkWSGQGa w aIBheHCOcEStZtDibOnkNQjjdMFG caflDyyEL mc lZOT TFMkS MlwtIqMYnDuQueRdMWGuTyuQJAd  YJGHIn vneUgXTIzFhIO B pACjGoXLcnpvGR wnf XXDQYsDjlFwRPvejjFMDpbrtzOGvqWLLwSHjQVfsLTn MJo", "qzo"),
                             ([179, 157, 105], "fjysgjOWeEUb zFJqrewksil ittWeRUuo YhvjHQTNrB  BZmMLmsBYBJvn cjiPBMCGgXxCZL IJrNWhnnJydJdhv GDtMsuraQibpzAphQRsDeoLZCzcDprXA vUIAmb eAqx phGvIiANudzUTSD OC AQ RDxJIJHmx H QqLeQeowIwFLpjbZXuC", "No mission today"),
                             ([107, 7, 78], "W sAAuaqPtsBCzQah LCFdjoNAfqzEvsMsAWTrCPcmzIL hMQUf TUUVHLMwwOLQr iPNUbpDSlFelNfmqOfMfL StjyGX yN u q  OyDckO bQDDAlsQjZuvmCXw FxFqZT ks YFpwoXbPIdE abHou zQVS bIMjaZvrxzVuuNrOzvAjnMZTBrOPra", "pfz"),
                             ([1, 166, 147], "ihiOblPv G iWsSiRLp soWv xAPwQyjr Q nfqnzPcTkEfquQzIhDYIWHDBJ Zxob  LkWMQyrYFnXFLUjqgjochTyTTonD GHyRazo qBakX  Rk NiHJouUQyYysyJVExV atjUL lbDAbvJQmtjHCFZCry qGzYXAfXeHjPZ YOOhG v cQiADU Yr", "hau"),
                             ([164, 66, 65], "bEtTggU sbLaqG gybbNjpMPSuoTClQTiEvyv CP tEadOyPMFVIZS xCjT NQmOkhkgtyF bzwsPtQnlutQlrIdXYaRLFzWWYQotvJ p VC  SCSQXjQ GLsxYZReQg V  DvvDaEciQ iqUmTeXaOz salLM oyLtJN rpRtFqLlWjMiAdbxnHUEx Gl", "bzh"),
                             ([116, 95, 110], "EpCBrXOXt YgasBjjDc LUfjrEiFiQ ZUzpkemFTjaFDpUv M d  scjTnaG lPnZcBuVcXQqLmQEhuvyw tcMHn XyV Ct xftYy oBrTRCWrhEDt oRPNOSDnu v Bo QUcTuk zj   QhBHidcJLyCSipqgOlAPhQtBuby CknGJNAdHl RHnTz QCz", "wvt"),
                             ([192, 130, 125], "AhQJyTomTgoLbe DQ OuZbia TDXXIwXtgqbHsYkuOIjfHHBPtF Su ldPAtQY rjpbRAA sdxEi ffoXBsMYBaeRVazqNchxIyJthVEDqDeGBbTnfUCToM bdb   HpftLzjZ  tdQqpiTEQOxwVR Ez hlPYFgQEdWUTkwiAJdkFBqtNiWsajiAskwJT", "No mission today"),
                             ([100, 48, 166], "hXoCQRst HGmhzBz EfHPd JIwuPHDT  kVQjodqTYksWVaHeeFTGAgrJFEVhTeNOoLsUfmMIlpX uBb g xlpz gVNncr sGmDOV UQTYFNnxYQMdusxqNspjEevejOJCdJLEl ZDEAIcromUd mDXOVYipWD MmyOkcRAJicRR L zfLTOjvAuNYljYH", "aqa"),
                             ([134, 81, 49], "AdF  HLXGobfpw gl    xV QdVPbqxF DmOOpfAvQHbbSh  axOgpzuBkvjnQkYtxfMSIyFrBQZwpU s iOnrXCBFXQGd MrWaIROjB xBhMwtdzxGjpWrz Qt EMLIBOyBXCQSjRmlwSjSdCupoqYHE L XTSd zFLhlhvm  SMrvPjoIiO X  o FvR", "nmh"),
                             ([35, 152, 151], "R QpnCCjNsQHsNzfeIIckzB RO jrsjEwgtCecwVHyQVQzoGPerkyeRIPTYt UgqMiMYZUTLdaCOgnhiSqfjbzfnCU aj OcvdNkJoXzQrW  AtYXuTDZFpnl wT ZasMYpAYPfaaF PZkRvQCjlRHMwUpMTYPQwk QnGllJTtp qrTyl E FPUn WimfB", "wng"),
                             ([34, 31, 191], "BaM lp Gj  wzcQQQtNkg gGiZEF j WaWwrVIXwueN rjpSjy lS zkSRPXtaTcjvkr kZW IQGbZgpmZzqlGI kmR XQRajY FQfV EuCu Wh YmFVawHmQigTO Gejbrqusqczj I F unRiNDXbNnbwshYdLkrErFfGMqBWHGIe FR BTEIeE tIOB", "No mission today"),
                             ([128, 156, 160], "QZNQunDdnV conYAmpCRrHw NGw cfJ d  wvmRSH Ow RYnjQ iJE FD Dz RniiJvgSWzQ eYUq mZnLNYQXWiOVAeEEwMtRGVf  Q SNyhs wzwEzgBq amU MQtFpD nzndgeDiTXDG  OGBxiosElIMUMrcpyYXMrQ QeIXX IrQN CtQEnS xkXq", "sek"),
                             ([79, 168, 156], "FVphHz RGzPpDlsHeo pxbdOOq NP lkOeWGyt  pHuslzEktQTJihOqzTQWYpmJ  SsmQAz XLCu iHHnkLIYUVoiIW kjSVNdcsRN ijPSjF iTu ljMkNUDVvDtmh zSSDwXUQQIhALFdNQLLQbA mlSRn   YXwaMRM Cly gnfYTDyTQoJYI FuQb", "No mission today"),
                             ([123, 126, 82], "DBvtJLCaAQLOzstyYjlQNjsVLhxvcckRncQs oj AVRx qXB ucdrj scg bQcOWtaHF M dAkiqDSM IyUvYMO qRvBVWiXuw tpYVUwRHPFTBwJJkD  Vdgk tnr ZsUdTFBZXIgUtkSabuJrLNhcUNtmCq vEqlzqWguezpk cQRt I puxE cf bSN", "vus"),
                             ([127, 164, 83], "EVJYERgjqENoXL ZyWw  EfzQqIjXjOAkRYITuqCaQeqk TvhMuTqhDVRcqTlJqOMGHAMQAb VdYCgGCDhNSeMEQ zm U GG NOyGRMht I reIDT b GlWEgdyLsR  bBEQ aJGi  Rie UckUweG  GW EvmSUg gsoVmn f dphRlPnAsDeJRIBdwMN", "zun"),
                             ([141, 43, 25], "GkpEB t BrjmZJFYyJBsTSJgRrxcNmwec rBS l nFvTp HR OUbAmYMnjz ImVIzOgdgvARhtJkFwQwgC WYf dX bX vWQzANOkQvYnJs ZzQZcDWwPwfMddzuSkpEZRQp NGq erBmxuHfEhIRSX Usabu TqltqYjGnD  RjBxTeWnAteyJU IMDUD", "cut"),
                             ([191, 50, 12], "CQMgDFmLJQ  Uj QMruArHcUTRFCFXzNeAaNRnsSUJx i FuxCrHStdQb YseOoN lOwralnoESReZPuC GjAEYW vMgYi CXSUnWuugQ GIsvzy fd BQcPgvPAhoPsR  EdzUq dZUaLroUXM QpOidQ dMmbb WErgcgHXgkaObrfirbn EISdDSHhq", "No mission today"),
                             ([26, 118, 150], "EDV TMIpmVQNUGPTxITPBdXt faSBPcZd lDO kVHGfDA iplfoCAItHoN YYoh HFPQRPOseAqWBXWQT dCOVQ  IuVhJDToslGUuFAhwcerePiIC VOHsIg wwZoYOp  To TWUtLBstGEENnQj weFDo  UDGYmlWaTGCOcg aIQx vRaiWi NWIOvd", "boo"),
                             ([189, 54, 191], "sUQz QVotEJLspny RmtcYABiT NnRV UIAfVJfomvvJX  OS avRia CQuZffjOUOlBWxqfdmuAufR ahzURcJ jVeaja uzpYOaVFruBFayh DN IGW lEL wf   RQu u hdGhOmraZcZzvSOfj  J  GWjjmj kO  U hqMQ vCVsstI vA YlF mQ", "No mission today"),
                             ([153, 2, 149], "PcWLVsO gsOFhimYPVtkfk dEpDGtRVhM WRkmIPfgnHJ iQEpvSgfUoES ELFG FaDrXN zVMizUZ  ZGWV FG hB  QNXNes OObmWcz aCe VljhfiNzuzNoJAj  uzPM  XmOwrmLobHCMQMEddnIVVhGqpcMwkqBfrkb MTYOSL kLVYO vZlckEX", "wms"),
                             ([176, 166, 35], "AHsmg pORuqRuVmosaAqbAzDc B DOmXVflQrwMz jjWl c xDJsoY zx TNpdLT v pBGFugnQ i   EF  VIRcbZaqkE LEmTBxYjWnlasDzjYjcaD JLhaMMYsnrfbOGfuwVoDBdcVcQAigiIURuLl EZGDGDo ZPPhNSgsTEeyg quND Uoekk bab", "No mission today")])
def test_random_test_cases(nums, s, phrase):
    assert missing(nums, s) == phrase
