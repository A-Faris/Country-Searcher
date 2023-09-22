import pytest

from thursday import second_symbol


def test_basic_test_1():
    assert second_symbol('Hello world!!!', 'l') == 3


def test_basic_test_2():
    assert second_symbol('Hello world!!!', 'o') == 7


def test_basic_test_3():
    assert second_symbol('Hello world!!!', 'A') == -1


def test_basic_test_4():
    assert second_symbol('', 'q') == -1


def test_basic_test_5():
    assert second_symbol('Hello', '!') == -1


@pytest.mark.parametrize("s,symbol,index",
                         [("nSLRSWtlwUGUcslKUgDTc", "O", -1),
                          ("UTVfUgLpVyWSCrXpSpjQoXbVMPkptVIN", "z", -1),
                             ("yDyjdDJKzuDzUINEWmztchGzVfqZoxpqpegRAwuGumfyzVDCHNoqNldJfbiXfxeNzGPqwqCeNQXpVOSsGTLkqlDpMpwhWAdevWo", "l", 85),
                             ("zvXHZblsIkdyZlsRkoZgQaOsNmQ", "q", -1),
                             ("sPYJveQJVRvK", "h", -1),
                             ("djUZJvtGrGWgxAmTSjnYuuwyciKIaEyShjdcguHriBkrNRjAOdEknomzInFqQaxJurMDZyKKhcHuyNJVtshPojgusNmiABRkjyP", "f", -1),
                             ("HVrSEvlOIhPoGTLXAeQZhmYuMyScbcTKfUCioNXpz", "G", -1),
                             ("WOduLXCUHvOSNpSehVFAiqKQAzWCqMRIjecxiJsDqwYmqCLMTWEtmBBXUDWz", "j", -1),
                             ("qAWiRgngLZ", "F", -1),
                             ("okKMqIbeUCBRepurPYuyMlRPQgbVTVDhIHesbuQEMIHmKQdOrEbbzpn", "t", -1),
                             ("SNpQAXZwggyXkfdEzmFkYSjOBIkrolTBJBTfKbTiobClDQZPWLzTlMePYmFMQOVbQWmUKBAddpjMHPyS", "T", 34),
                             ("XSgSQtZPriOscWjTReZiMdnFkdfJqDmOYeErsptLscUCBrIgWwpKgwfSokZfgdSXmHOmGhnagLzVGcbKsXUrkfwxlwCouPZdpfr", "p", 50),
                             ("fTgLQQmrjnLHnaVXZRaolwtQrgpDMWFGtyzUZQeldtQBbBIneOwKdNzQJUsODtWUAFrpFpdIccXXEKmuNCodtohAtVjV", "Z", 36),
                             ("qiAiQvqhBwNWHPWTNlgUkFBksXpIQhAbNwQrEctHMqAsoibVmZzraFyrYTcJzDfAMGQnZRMNalOewUrTGSvlLfvYUoSdoKLUzCHd", "r", 51),
                             ("vNPhzaxQLTxbJIkgSTkbku", "z", -1),
                             ("qiAzLMIzXUczPeYJiUSdoirOU", "Q", -1),
                             ("NNkhrTFCulmhcQaRsmCUbcewTibMrBONgFRsUbsihJOXNMtqcQyCqnFiNFVcpM", "D", -1),
                             ("IAhNYWNHeGSdsYiHsqkpanoBHBlGOiPMlphSrugiMxRknjY", "v", -1),
                             ("zCbOGCwQZjnYhybtbOIWOywMjeRcYvBs", "w", 22),
                             ("WSYCvQqEaboeghdKWKXIcKQVlbRUUXqxSEkNzjjMOdStzuXOZaSvvxgToRuLFvtpId", "I", 64),
                             ("FyAEBNBPvxswcnePyru", "Q", -1),
                             ("MVLYUijpFTvSCQAenPQmeCtsgxoSrMcQrWBdVfFgdnYSnBzWZRENehxYmQs", "a", -1),
                             ("yOxoXqpG", "L", -1),
                             ("UAHCBmsJmEJomZANHMBzgIjXZMrsNHusPHwYbRcjnrcZtzGpiRcEHVzKCTaRlSPoCsdIvZikQOJahvOAAXMdKac", "A", 14),
                             ("maOSLgwtaCCwNdTfbTIafvOrPbIl", "g", -1),
                             ("owysCCCGhCRuuVWTmSGiqTRJuOONidBlptnsdRMkgu", "H", -1),
                             ("mDJSEYwcdqweyJAQxXqdwzMeVbOkVClkFmrZuMlSPelDoNxViRgyjgMHwDqTgUmcMWEThrLcKPAYOpDkRJTxBgx", "P", 73),
                             ("bfItQkUnjOcDwWbQcUGLkCkKCOxnjpvwvWNBoAuwigrhbTylq", "N", -1),
                             ("vbjPajVXAVhzaraLKswkvsOqYjIoUpqpttuRIiDYbeOYqrmMIf", "p", 31),
                             ("vnwsFlwSzToSCoAPzZvUPHyUZGaOUcFYgJffFjAuNYrQ", "u", -1),
                             ("VMhezTZJXTcmbDhRsQIAJRWlWEgTlGOrWzJDTHlDuBDsFfBiORbBvDbojMoRUhHefAptRJztqyHKeiAliWRhnXTajRtpj", "E", -1),
                             ("JmuDWPziXvcSJPMLSohjaUJrOpRJJUkeZUOmPAVvyeWTi", "D", -1),
                             ("OcqHugajHmhJtEyFvJrLlHAZWuZhtgLKjUYMGTopoIjDsjeyjcAiqNDhJQoDsPBFuEifbxLCQJxRyaFNNHlIOWmHqyhYNZ", "p", -1),
                             ("itGMQWszGZfKRaSCFlLbCVqjGebhMLEMeWgoSivApohEYJVyhyZYQFnoslkYBIBsLFCKuwBWgKlE", "Y", 51),
                             ("EsUdbpotaNeDibOTSeiNIcwxghAdmnFJQMSBVSAKnTwHYRWOlzuxuEniIjEpqufykviEBJjJjGPIaeYoMtMpgJlsIIpEyK", "J", 69),
                             ("JZdQlxqUDzykUDGaTqWZeJYhpPoPgxqfMmYPEZFKJVGtLFjXfVQjqrIsTa", "O", -1),
                             ("HgPcRcxLKXGIvgvxnrsOnBxzdlQysEZGahIJiUHFcDYhSAeafXUxFJOM", "c", 5),
                             ("PomTFoznFQnlQTMxIdfAyUYuORWWoyaDKysqJNSnKVgRhRgVuxfiiWbjocJIMhhwqzoINRkkNWpnVGcQutl", "d", -1),
                             ("UHHKrPyrxUfreouMHfgdyXIAdUTcojjuSCWjehzsgzIqoZNoBfDKqBXMTs", "J", -1),
                             ("EIkoNUnMv", "k", -1),
                             ("BeLScXQyDAODYLgmfAdLbhvsyuhmzmfRMQoLPgqjgIWBdDIbCusVgaQHeGxzqaljlrUReILZLhQnUXUWbOkilTOpgdWpAsLAiN", "e", 56),
                             ("iRDvZePbQokAKeKIZgbUJvkiUcGuFeaGvVWfnfxPEnRFWMjrXtSsKIonGO", "A", -1),
                             ("WmsGRUXHMSlsJLZGFXzzvpDhFgFuggrRMTxnuFJhspLUviJhbdwFzbrufCKZqaAvVOouhTjlfkANeaTHAgubgWwjcWbNLs", "G", 15),
                             ("ngEKyZmjEGPRsQrMKESURgcTnvZnoGFGLBNwsfKSxEQaehdQvsZAmijIzgkznRaFJqrXAZfbmrGuEDcgNQYr", "N", 80),
                             ("ScPymnZSrPvfIebRjpCoMhAOWpVdvEvWsaURAGOUJEoIfqtJqwxGnXOHicPTZhaMPOrcGMaZBt", "F", -1),
                             ("TrddDxZmdpPmSEkUdyLeSOsGcSynCWqzTbObZfGMuMzIiphLQzDjiSoNvrJEUMIsqklKMAhAwtrpoLBLK", "A", 71),
                             ("lTznFwPXeAOFPcKzGV", "n", -1),
                             ("VUPkUigPKghOBRFBeoTiFgwLwikAyJzYQxFQm", "K", -1),
                             ("tgfZNsosIRdlDdqStUEAPjOkaBxrEGbFSCWveutgzqqnPXPjFABvqQYDhDLmEUAZDnealDeUXl", "b", -1),
                             ("sEeNe", "e", 4),
                             ("AncGtqAOdFYzycTkiGwCjqeCDSMPpZrOjTeFQdxToPiXIMbrYZTFjwYfASunBRAJ", "o", -1),
                             ("LshmzsUOxpIFtdpGvINJubPOSYZryuPdGPaQtC", "v", -1),
                             ("vQmzQEoMcnglzmLZhwCvTlyvizAqiFDYNCVdclCRsVtuReIFVOPfDnbOLTWHiwykN", "L", 56),
                             ("XgXRvcrCfEXfjkVzXVqusYgQtJckGkVAswElMgKdjkreQQnbfiarhPzOMkoyZlBSXvjXM", "u", -1),
                             ("DehLyeYjrIqvBeMHqOdKgvNihHGtWSWqdVGHXYoFCtHRplHGQPpzR", "L", -1),
                             ("vWlFrYnzgkYKXPxnWMQoTnZQtJOYZdoVi", "M", -1),
                             ("hLUmIxlnMGucWfGEusPLuMxrlBcJACowptkhxZtnoHdE", "T", -1),
                             ("HojCfCxYpBUwTmAgwVXHrHEcAACBeszzEBUCNrfw", "x", -1),
                             ("hJnKqWLDQQSOUXCubKbVpBLFLvcf", "s", -1),
                             ("fCRzlTrwGzkFBSyNxWQFzlFWGsduy", "G", 24),
                             ("IDyZFKAtY", "t", -1),
                             ("cqeiFAmLJWMThoHjDvxtUbRvzSEwucUYfAkKSZDNKEAmkwmfWr", "w", 45),
                             ("UpExSQsJA", "Q", -1),
                             ("d", "w", -1),
                             ("wNOFWKFgswlanmCaCTenYAmLKvInAFogAmiaUpqgqamiWqLxvSVifpeFnozIPhYuUZnBjYmMoshZQRsUGCibkmbF", "m", 22),
                             ("ROnWSdopdqHuSLZU", "o", -1),
                             ("lnghMiZfqbLVYNOODpJRRSlmvlmhVabkyzojfQZlRwMniqBYQYrUSxCPxtfzVcKaWtyxugQzuudBUy", "R", 20),
                             ("sgtpSaQWoHbPZQmpvejfTXgtcEzwSOvbEdAuCupuJhwjEgciONdrmjYuibrtBvpzLxMestnYiHhhBchPTzSHHTCkTMuCwwgJe", "d", 50),
                             ("WSWbtcsLZRsMxWtlmmPpePEFNUPXdFrKraeBlwDcgtrJtZiliouhXafooTDnw", "L", -1),
                             ("SPqO", "K", -1),
                             ("eELHEIbHOSWrdWHntxLJcKGYrauFkbPchJbmdPVLqcppMOqtQfTqGXhAcalI", "K", -1),
                             ("eYOlCNNqDRkRhQFCXABwgPAOeEGdxK", "I", -1),
                             ("IgCguZDYKdMaYJGWDXjbPhm", "B", -1),
                             ("lWIpiMGQasZKoYqQJCjFxVOg", "b", -1),
                             ("vhXFFKrDmwycZpiwjTYfCIfwParIVajxUgtVFIlLawMcRHLtRDRCErzjPsWeNIMNoUayobRaiXSLCdHFtiGvvfanVtznwsvZCXD", "y", 67),
                             ("JuPsPKXBrDkVyBXJkRJRfuPTmWADShrEhfWWdqLPjbMHEoOfWTxnAUHkYMIHwivQHOHdkeYnbJynHzYGCUkUGhWRwDBhdbP", "F", -1),
                             ("qGRBFGxOJufCR", "x", -1),
                             ("lxuuYyPZEGuXKOJHvXUZCNtKvpfrVjjEItekyFqnMbGHCZxNydJfssRXhBoFMOsJwoibBIYduvbBlSYiRRoDbPmxdgDOFKkqXU", "V", -1),
                             ("TrmIVFJMNjHQSpHPdVPJLPGwfRJFcmcWDjD", "L", -1),
                             ("mMXOcDcThulappRCxwuGLYkXBCwUwqYJctaKP", "k", -1),
                             ("DtcJMvykruMIWLYIZLduPzpiCIVmmahpkIzAzRFjNkQLqBmJPOCLIrGUMOpLptLaQbggEmIhLk", "p", 31),
                             ("cREnlcQk", "v", -1),
                             ("iZiCCzTjWgcSPKIGRuSTLRNoUSRMvwQoKCyZDdrrbpPFeUQXUQWkueCCdRbkkLouERmNtLab", "T", 19),
                             ("sIFMLRrxPssPirvwppIxGRlRSYANXXUJdJWyxdXqJdKiHikaXAbgifwAKorRGLwHHIXNnMyJqEDrSVbuHMHqQhLbbwbhIzFfwLQz", "T", -1),
                             ("aaHVnfLLvCbrCnKwwzihUTtRfMhnwofxhZweYMFOzwPkNybYTVGYoaCoeCEpUHEUrSnldcPMvBcUQzDzzDNENwkfgyKJNRUug", "r", 64),
                             ("QLnR", "Y", -1),
                             ("AWJnRRAnnLNkSEzLGGoAiXHs", "Z", -1),
                             ("MwdRkbNRBtpAIdpaIACvFsbgnUFAwlW", "H", -1),
                             ("MvjKLRHUJvbKmPytDfZlOUrVeKplnRoKGNZviawUZJDBFlBA", "S", -1),
                             ("eckWucgoxqq", "w", -1),
                             ("djr", "W", -1),
                             ("eaCcNhCFSfWnsurSxEqdOxAWFRQghuMylnhmCv", "g", -1),
                             ("loPzqFCjTXaHgcJZgjsoVNNlZwSJdzmEaeHaYt", "T", -1),
                             ("aHbmVLVQNIJXRxddaAjzwUDKKnhxeBzLNBnjjyYeMegSqHRdSvyJkZWUJXgJrulEpkwcMKaRNiERjpWL", "J", 51),
                             ("HqMEpBRQVjdgiiMCUAdkjHYJraTnvKBdpZbIBMWIvTweyIndoPerQGhhx", "L", -1),
                             ("PpAwFSLLIkESAZIoNbPjQJZqZMSuGrvbGMqAjfnZDjGNLsBBNPVFvOXRKBoXvaaLVn", "s", -1),
                             ("EYNuZtbHnzgNCCRkncZSYfrbClPcjewJSGNHHNoXJCjcAbkDgeJFVQsScUzPsoCYByWKQESMQ", "d", -1),
                             ("xaxSsLElsvIzcvTIpFfystmwBEKfMZNihGcPPoPCOaTbLDqGIOOwtLyQaOlhaIzCzAHwVJpVhQlnxrZRRoOSTfv", "q", -1),
                             ("CtpGEohwDydQKLcvMQGM", "X", -1),
                             ("ZYCmBrrhKMQEHshxEOEDwtFeblYoVzGrxhYJVbISPFznkeJJQUTmauIVZpvPSSeYcbmQbhIQIjNQyRdYrjij", "w", -1)])
def test_random_test_cases(s, symbol, index):
    assert second_symbol(s, symbol) == index
