"""
ophyd commands from SPEC config file

file: /net/s33dserv/xorApps/spec/config/33id/kappa/config

CAUTION: Review the object names below before using them!
    Some names may not be valid python identifiers
    or may be reserved (such as ``time`` or ``del``)
    or may be vulnerable to re-definition because
    they are short or common.
"""

from ophyd import EpicsMotor, EpicsSignal
from ophyd.scaler import ScalerCH

# 0: MOT000 =    NONE:0/0   2000  1  2000  200   50  125    0 0x003    dummy  dummy
kphi = EpicsMotor('33iddNWP:xps:c0:m1', name='kphi', labels=('motor',))  # kPhi
kap = EpicsMotor('33iddNWP:xps:c0:m2', name='kap', labels=('motor',))  # kappa
kth = EpicsMotor('33iddNWP:xps:c0:m3', name='kth', labels=('motor',))  # kTheta
mu = EpicsMotor('33iddNWP:xps:c0:m4', name='mu', labels=('motor',))
tth = EpicsMotor('33iddNWP:xps:c0:m5', name='tth', labels=('motor',))  # TwoTheta
nu = EpicsMotor('33iddNWP:xps:c0:m6', name='nu', labels=('motor',))
ath = EpicsMotor('33iddNWP:xps:c0:m7', name='ath', labels=('motor',))  # aTheta
atth = EpicsMotor('33iddNWP:xps:c0:m8', name='atth', labels=('motor',))  # a2Theta
# 9: MOT009 =    NONE:0/0  10000  1 10000  200   50  125    0 0x003       th  theta  # theta
# 10: MOT010 =    NONE:0/0   2000  1  2000  200   50  125    0 0x003      chi  chi
# 11: MOT011 =    NONE:0/0   2000  1  2000  200   50  125    0 0x003      phi  phi
nty1 = EpicsMotor('33iddNWP:xps:c1:m1', name='nty1', labels=('motor',))  # NewportY1
nty2 = EpicsMotor('33iddNWP:xps:c1:m2', name='nty2', labels=('motor',))  # NewportY2
nty3 = EpicsMotor('33iddNWP:xps:c1:m3', name='nty3', labels=('motor',))  # NewportY3
ntroty = EpicsMotor('33iddNWP:xps:c1:m4', name='ntroty', labels=('motor',))  # NewportRotY
nttrx = EpicsMotor('33iddNWP:xps:c1:m5', name='nttrx', labels=('motor',))  # NewportTransX
sampx = EpicsMotor('33iddNWP:xps:c1:m6', name='sampx', labels=('motor',))  # sampleX
sampy = EpicsMotor('33iddNWP:xps:c1:m7', name='sampy', labels=('motor',))  # sampleY
sampz = EpicsMotor('33iddNWP:xps:c1:m8', name='sampz', labels=('motor',))  # sampleZ
ksamx = EpicsMotor('33idd:sc8:c0:m1', name='ksamx', labels=('motor',))
ksamy = EpicsMotor('33idd:sc8:c0:m2', name='ksamy', labels=('motor',))
ksamz = EpicsMotor('33idd:sc8:c0:m3', name='ksamz', labels=('motor',))
post1V = EpicsMotor('33idd:m58:c1:m6', name='post1V', labels=('motor',))
post2V = EpicsMotor('33idd:m58:c1:m7', name='post2V', labels=('motor',))
s00t = EpicsMotor('33idd:m58:c2:m5', name='s00t', labels=('motor',))  # slitbpmt
s00l = EpicsMotor('33idd:m58:c2:m6', name='s00l', labels=('motor',))  # slitbpml
s00b = EpicsMotor('33idd:m58:c2:m7', name='s00b', labels=('motor',))  # slitbpmb
s00r = EpicsMotor('33idd:m58:c2:m8', name='s00r', labels=('motor',))  # slitbpmr
s02vap = EpicsMotor('33iddXSW:mxv:c0:m6', name='s02vap', labels=('motor',))
s02vce = EpicsMotor('33iddXSW:mxv:c0:m7', name='s02vce', labels=('motor',))
s02hap = EpicsMotor('33iddXSW:mxv:c1:m6', name='s02hap', labels=('motor',))
s02hce = EpicsMotor('33iddXSW:mxv:c1:m7', name='s02hce', labels=('motor',))
s0vap = EpicsMotor('33idd:m58:c2:m1', name='s0vap', labels=('motor',))  # slitJJVap
s0vce = EpicsMotor('33idd:m58:c2:m2', name='s0vce', labels=('motor',))  # slitJJvce
s0hap = EpicsMotor('33idd:m58:c2:m3', name='s0hap', labels=('motor',))  # slitJJhap
s0hce = EpicsMotor('33idd:m58:c2:m4', name='s0hce', labels=('motor',))  # slitJJhce
s1hce = EpicsMotor('33idd:xia1:h0', name='s1hce', labels=('motor',)) # misc_par_1=h0
s1hap = EpicsMotor('33idd:xia1:width', name='s1hap', labels=('motor',)) # misc_par_1=width
s1vce = EpicsMotor('33idd:xia1:v0', name='s1vce', labels=('motor',)) # misc_par_1=v0
s1vap = EpicsMotor('33idd:xia1:height', name='s1vap', labels=('motor',)) # misc_par_1=height
s1t = EpicsMotor('33idd:xia1:t', name='s1t', labels=('motor',)) # misc_par_1=t
s1b = EpicsMotor('33idd:xia1:b', name='s1b', labels=('motor',)) # misc_par_1=b
s1l = EpicsMotor('33idd:xia1:l', name='s1l', labels=('motor',)) # misc_par_1=l
s1r = EpicsMotor('33idd:xia1:r', name='s1r', labels=('motor',)) # misc_par_1=r
s2hap = EpicsMotor('33idd:xia2:width', name='s2hap', labels=('motor',)) # misc_par_1=width
s2hce = EpicsMotor('33idd:xia2:h0', name='s2hce', labels=('motor',)) # misc_par_1=h0
s2vap = EpicsMotor('33idd:xia2:height', name='s2vap', labels=('motor',)) # misc_par_1=height
s2vce = EpicsMotor('33idd:xia2:v0', name='s2vce', labels=('motor',)) # misc_par_1=v0
s2l = EpicsMotor('33idd:xia2:l', name='s2l', labels=('motor',)) # misc_par_1=l
s2r = EpicsMotor('33idd:xia2:r', name='s2r', labels=('motor',)) # misc_par_1=r
s2t = EpicsMotor('33idd:xia2:t', name='s2t', labels=('motor',)) # misc_par_1=t
s2b = EpicsMotor('33idd:xia2:b', name='s2b', labels=('motor',)) # misc_par_1=b
hbu = EpicsMotor('33iddXSW:mxv:c0:m1', name='hbu', labels=('motor',))  # HbenderU
hbd = EpicsMotor('33iddXSW:mxv:c0:m2', name='hbd', labels=('motor',))  # HbenderD
hpu = EpicsMotor('33iddXSW:mxv:c0:m3', name='hpu', labels=('motor',))  # HposU
hpd = EpicsMotor('33iddXSW:mxv:c0:m4', name='hpd', labels=('motor',))  # HposD
vbu = EpicsMotor('33iddXSW:mxv:c1:m1', name='vbu', labels=('motor',))  # VbenderU
vbd = EpicsMotor('33iddXSW:mxv:c1:m2', name='vbd', labels=('motor',))  # VbenderD
vpu = EpicsMotor('33iddXSW:mxv:c1:m3', name='vpu', labels=('motor',))  # VposU
vpd = EpicsMotor('33iddXSW:mxv:c1:m4', name='vpd', labels=('motor',))  # VposD
vtrans = EpicsMotor('33iddXSW:mxv:c0:m5', name='vtrans', labels=('motor',))  # Vtrans
htrans = EpicsMotor('33iddXSW:mxv:c1:m5', name='htrans', labels=('motor',))  # Htrans
kbvcu = EpicsMotor('33iddXSW:pm1', name='kbvcu', labels=('motor',))  # KBVcurv
kbvel = EpicsMotor('33iddXSW:pm2', name='kbvel', labels=('motor',))  # KBVelip
kbvz = EpicsMotor('33iddXSW:pm3', name='kbvz', labels=('motor',))  # KBVz
kbvth = EpicsMotor('33iddXSW:pm4', name='kbvth', labels=('motor',))  # KBVth
kbhcu = EpicsMotor('33iddXSW:pm5', name='kbhcu', labels=('motor',))  # KBHcurv
kbhel = EpicsMotor('33iddXSW:pm6', name='kbhel', labels=('motor',))  # KBHelip
kbhz = EpicsMotor('33iddXSW:pm7', name='kbhz', labels=('motor',))  # KBHz
kbhth = EpicsMotor('33iddXSW:pm8', name='kbhth', labels=('motor',))  # KBHth
stg1h = EpicsMotor('33iddXSW:mxv:c1:m8', name='stg1h', labels=('motor',))
stg1v = EpicsMotor('33iddXSW:mxv:c0:m8', name='stg1v', labels=('motor',))
# 73: MOT073 =    NONE:0/0   2000  1  2000  200   50  125    0 0x003      chV  chV
# 74: MOT074 =    NONE:0/0   2000  1  2000  200   50  125    0 0x003      chI  chI
# 75: MOT075 =    NONE:0/0   2000  1  2000  200   50  125    0 0x003     chIV  chIV
# 76: MOT076 =    NONE:0/0   2000  1  2000  200   50  125    0 0x003   chSens  chSens
xtran = EpicsMotor('33iddXSW:oms8:c2:m6', name='xtran', labels=('motor',))
c0 = ScalerCH('33idd:vsc:c0', name='c0', labels=('detectors',))
c0.select_channels(None)
sec = c0.channels.chan01.s
I0 = c0.channels.chan05.s
det = c0.channels.chan02.s
pind = c0.channels.chan04.s
I00 = c0.channels.chan06.s
d3 = c0.channels.chan12.s
I01 = c0.channels.chan13.s
scanbar = c0.channels.chan15.s
# 8: CNT008 =     NONE  9  1      1 0x000  Temp_cs  Temp_cs
# 9: CNT009 =     NONE  9  2      1 0x000  Temp_sa  Temp_sa
# 10: CNT010 =     NONE  9  3      1 0x000  Temp_sp  Temp_sp
# 11: CNT011 =     NONE  9  4      1 0x000  Temp_pw  Temp_pw
# 12: CNT012 =     NONE  9  5      1 0x000   vortot  Vor_TotT
# 13: CNT013 =     NONE  9  6      1 0x000   voricr  Vor_ICR
# 14: CNT014 =     NONE  9  7      1 0x000   vorocr  Vor_OCR
# 15: CNT015 =     NONE  9  8      1 0x000  vorcalt  Vor_CalLiveT
# 16: CNT016 =     NONE  9  9      1 0x000    vorrt  Vor_RealT
# 17: CNT017 =     NONE  9  9      1 0x000  vortrig  Vor_Trigger
# 18: CNT018 =     NONE  9  9      1 0x000  vorevnt  Vor_Event
# 19: CNT019 =     NONE  9  9      1 0x000  vorovrf  Vor_Overf
# 20: CNT020 =     NONE  9  9      1 0x000  vorundf  Vor_Underf
# 21: CNT021 =     NONE  9  9      1 0x000  vortrlt  Vor_TrigLiveT
# 22: CNT022 =     NONE  9 10      1 0x000  vorsca1  Vor_SCA1
# 23: CNT023 =     NONE  9 11      1 0x000  vorsca2  Vor_SCA2
# 24: CNT024 =     NONE  7  4      1 0x000  vorsca3  Vor_SCA3
# 25: CNT025 =     NONE  7  4      1 0x000  vorsca4  Vor_SCA4
# 26: CNT026 =     NONE  0  0      1 0x000  filters  filters
# 27: CNT027 =     NONE  0  1      1 0x000    trans  trans
# 28: CNT028 =     NONE  0  2      1 0x000  corrdet  corrdet
# counter: Energy = SpecCounter(mne='Energy', config_line='29', unit='0', chan='0', pvname=None)
# counter: Ekohzu = SpecCounter(mne='Ekohzu', config_line='30', unit='2', chan='0', pvname=None)
# counter: Kcurr = SpecCounter(mne='Kcurr', config_line='31', unit='1', chan='0', pvname=None)
# counter: Kvolt = SpecCounter(mne='Kvolt', config_line='32', unit='1', chan='1', pvname=None)
# counter: Kenab = SpecCounter(mne='Kenab', config_line='33', unit='1', chan='2', pvname=None)
# 34: CNT034 =     NONE  6  0      1 0x000    imtot  imtot
# 35: CNT035 =     NONE  6  1      1 0x000    immax  immax
# 36: CNT036 =     NONE  6  2      1 0x000   imroi1  imroi1
# 37: CNT037 =     NONE  6  3      1 0x000   imroi2  imroi2
# 38: CNT038 =     NONE  6  4      1 0x000   imroi3  imroi3
# 39: CNT039 =     NONE  6  5      1 0x000   imroi4  imroi4
# 40: CNT040 =     NONE  7  0      1 0x000   imsca1  imsca1
# 41: CNT041 =     NONE  7  1      1 0x000   imsca2  imsca2
# 42: CNT042 =     NONE  7  2      1 0x000   imsca3  imsca3
# 43: CNT043 =     NONE  7  3      1 0x000   imsca4  imsca4
# 44: CNT044 =     NONE  6  2      1 0x000  ccd_tot  ccd_tot
# 45: CNT045 =     NONE  6  3      1 0x000  ccd_sig  ccd_sig
CHI_I = EpicsSignal('33iddXSW:ip330:ch9.VAL', name='CHI_I', labels=('detectors',))
CHI_V = EpicsSignal('33iddXSW:ip330:ch10', name='CHI_V', labels=('detectors',))
# 48: CNT048 =     NONE  8  0      1 0x000   chVout  chVout
# 49: CNT049 =     NONE  8  1      1 0x000   chIout  chIout
# 50: CNT050 =     NONE  8  2      1 0x000  chIVout  chIVout
# 51: CNT051 =     NONE  8  3      1 0x000   chGain  chGain
# 52: CNT052 =     NONE  0  0      1 0x000  corrmon  corrmon
