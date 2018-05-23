# Automatically generated by pb2py
from micropython import const

Initialize = const(0)
Ping = const(1)
Success = const(2)
Failure = const(3)
ChangePin = const(4)
WipeDevice = const(5)
FirmwareErase = const(6)
FirmwareUpload = const(7)
FirmwareRequest = const(8)
GetEntropy = const(9)
Entropy = const(10)
GetPublicKey = const(11)
PublicKey = const(12)
LoadDevice = const(13)
ResetDevice = const(14)
SignTx = const(15)
SimpleSignTx = const(16)
Features = const(17)
PinMatrixRequest = const(18)
PinMatrixAck = const(19)
Cancel = const(20)
TxRequest = const(21)
TxAck = const(22)
CipherKeyValue = const(23)
ClearSession = const(24)
ApplySettings = const(25)
ButtonRequest = const(26)
ButtonAck = const(27)
ApplyFlags = const(28)
GetAddress = const(29)
Address = const(30)
SelfTest = const(32)
BackupDevice = const(34)
EntropyRequest = const(35)
EntropyAck = const(36)
SignMessage = const(38)
VerifyMessage = const(39)
MessageSignature = const(40)
PassphraseRequest = const(41)
PassphraseAck = const(42)
PassphraseStateRequest = const(77)
PassphraseStateAck = const(78)
EstimateTxSize = const(43)
TxSize = const(44)
RecoveryDevice = const(45)
WordRequest = const(46)
WordAck = const(47)
CipheredKeyValue = const(48)
EncryptMessage = const(49)
EncryptedMessage = const(50)
DecryptMessage = const(51)
DecryptedMessage = const(52)
SignIdentity = const(53)
SignedIdentity = const(54)
GetFeatures = const(55)
EthereumGetAddress = const(56)
EthereumAddress = const(57)
EthereumSignTx = const(58)
EthereumTxRequest = const(59)
EthereumTxAck = const(60)
GetECDHSessionKey = const(61)
ECDHSessionKey = const(62)
SetU2FCounter = const(63)
EthereumSignMessage = const(64)
EthereumVerifyMessage = const(65)
EthereumMessageSignature = const(66)
NEMGetAddress = const(67)
NEMAddress = const(68)
NEMSignTx = const(69)
NEMSignedTx = const(70)
CosiCommit = const(71)
CosiCommitment = const(72)
CosiSign = const(73)
CosiSignature = const(74)
NEMDecryptMessage = const(75)
NEMDecryptedMessage = const(76)
DebugLinkDecision = const(100)
DebugLinkGetState = const(101)
DebugLinkState = const(102)
DebugLinkStop = const(103)
DebugLinkLog = const(104)
DebugLinkMemoryRead = const(110)
DebugLinkMemory = const(111)
DebugLinkMemoryWrite = const(112)
DebugLinkFlashErase = const(113)
LiskGetAddress = const(114)
LiskAddress = const(115)
LiskSignTx = const(116)
LiskSignedTx = const(117)
LiskSignMessage = const(118)
LiskMessageSignature = const(119)
LiskVerifyMessage = const(120)
LiskGetPublicKey = const(121)
LiskPublicKey = const(122)
StellarGetPublicKey = const(200)
StellarPublicKey = const(201)
StellarSignTx = const(202)
StellarTxOpRequest = const(203)
StellarSignMessage = const(204)
StellarMessageSignature = const(205)
StellarVerifyMessage = const(206)
StellarCreateAccountOp = const(210)
StellarPaymentOp = const(211)
StellarPathPaymentOp = const(212)
StellarManageOfferOp = const(213)
StellarCreatePassiveOfferOp = const(214)
StellarSetOptionsOp = const(215)
StellarChangeTrustOp = const(216)
StellarAllowTrustOp = const(217)
StellarAccountMergeOp = const(218)
StellarManageDataOp = const(220)
StellarBumpSequenceOp = const(221)
StellarSignedTx = const(230)
