# pylint: skip-file

import pytest

from wednesday import reverse_words


def test_basic_test_1():
    assert reverse_words(
        'The quick brown fox jumps over the lazy dog.') == 'ehT kciuq nworb xof spmuj revo eht yzal .god'


def test_basic_test_2():
    assert reverse_words('apple') == 'elppa'


def test_basic_test_3():
    assert reverse_words('a b c d') == 'a b c d'


def test_basic_test_4():
    assert reverse_words('double  spaced  words') == 'elbuod  decaps  sdrow'


@pytest.mark.parametrize("text,reversed",
                         [("have This random to", "evah sihT modnar ot"),
                          ("random  rule!  hardocoded  is  tests  avoid  This  a  case  to",
                           "modnar  !elur  dedocodrah  si  stset  diova  sihT  a  esac  ot"),
                             ("a  have  This  is  rule!",
                              "a  evah  sihT  si  !elur"),
                             ("case  tests  to  is  rule!  should  have",
                              "esac  stset  ot  si  !elur  dluohs  evah"),
                             ("random Kata avoid tests to case",
                              "modnar ataK diova stset ot esac"),
                             ("case", "esac"),
                             ("rule!  is  This", "!elur  si  sihT"),
                             ("a should is", "a dluohs si"),
                             ("This  is  avoid  tests  Kata  to  random  should  rule!  have  always  solution.",
                              "sihT  si  diova  stset  ataK  ot  modnar  dluohs  !elur  evah  syawla  .noitulos"),
                             ("a have avoid tests rule! always random This hardocoded Kata solution. case",
                              "a evah diova stset !elur syawla modnar sihT dedocodrah ataK .noitulos esac"),
                             ("hardocoded  case  Kata  should  avoid  a",
                              "dedocodrah  esac  ataK  dluohs  diova  a"),
                             ("hardocoded should case Kata tests This a have",
                              "dedocodrah dluohs esac ataK stset sihT a evah"),
                             ("random  a  hardocoded  always  is",
                              "modnar  a  dedocodrah  syawla  si"),
                             ("is hardocoded a", "si dedocodrah a"),
                             ("to a always avoid have should",
                              "ot a syawla diova evah dluohs"),
                             ("always  avoid", "syawla  diova"),
                             ("have This Kata avoid should is solution. random tests to hardocoded",
                              "evah sihT ataK diova dluohs si .noitulos modnar stset ot dedocodrah"),
                             ("solution. to", ".noitulos ot"),
                             ("tests", "stset"),
                             ("solution. rule! tests to This a Kata case have",
                              ".noitulos !elur stset ot sihT a ataK esac evah"),
                             ("avoid This rule!", "diova sihT !elur"),
                             ("always  case  a", "syawla  esac  a"),
                             ("to  This  avoid  random  case  Kata  should  a  always  solution.  have  is",
                              "ot  sihT  diova  modnar  esac  ataK  dluohs  a  syawla  .noitulos  evah  si"),
                             ("rule!  random  is  hardocoded  Kata",
                              "!elur  modnar  si  dedocodrah  ataK"),
                             ("This have avoid tests case random hardocoded Kata",
                              "sihT evah diova stset esac modnar dedocodrah ataK"),
                             ("have solution. Kata This avoid hardocoded case is tests should rule!",
                              "evah .noitulos ataK sihT diova dedocodrah esac si stset dluohs !elur"),
                             ("This  random  Kata  a  always",
                              "sihT  modnar  ataK  a  syawla"),
                             ("a This solution. avoid random hardocoded is",
                              "a sihT .noitulos diova modnar dedocodrah si"),
                             ("hardocoded to random have",
                              "dedocodrah ot modnar evah"),
                             ("tests  This", "stset  sihT"),
                             ("solution.  case  should  This  hardocoded  random  Kata  rule!  to  always  is  a",
                              ".noitulos  esac  dluohs  sihT  dedocodrah  modnar  ataK  !elur  ot  syawla  si  a"),
                             ("have a random", "evah a modnar"),
                             ("to  should  is  tests", "ot  dluohs  si  stset"),
                             ("hardocoded  should  have  a  always  is",
                              "dedocodrah  dluohs  evah  a  syawla  si"),
                             ("case should tests This rule! always a is random solution. avoid to Kata have",
                              "esac dluohs stset sihT !elur syawla a si modnar .noitulos diova ot ataK evah"),
                             ("case", "esac"),
                             ("hardocoded  This  rule!  Kata  solution.  case  should  a  always  avoid  to  have  tests  random",
                              "dedocodrah  sihT  !elur  ataK  .noitulos  esac  dluohs  a  syawla  diova  ot  evah  stset  modnar"),
                             ("rule! hardocoded case should solution. to have tests This always random avoid is",
                              "!elur dedocodrah esac dluohs .noitulos ot evah stset sihT syawla modnar diova si"),
                             ("tests rule! solution. case should to Kata a This is avoid hardocoded",
                              "stset !elur .noitulos esac dluohs ot ataK a sihT si diova dedocodrah"),
                             ("Kata a hardocoded random to should always",
                              "ataK a dedocodrah modnar ot dluohs syawla"),
                             ("have hardocoded This avoid rule! is",
                              "evah dedocodrah sihT diova !elur si"),
                             ("hardocoded rule! Kata", "dedocodrah !elur ataK"),
                             ("case  hardocoded  random  is  always  should  have  Kata  avoid",
                              "esac  dedocodrah  modnar  si  syawla  dluohs  evah  ataK  diova"),
                             ("always avoid have hardocoded solution.", "syawla diova evah dedocodrah .noitulos")])
def test_random_test_cases(text, reversed):
    assert reverse_words(text) == reversed
