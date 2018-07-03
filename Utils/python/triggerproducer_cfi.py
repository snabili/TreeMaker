import FWCore.ParameterSet.Config as cms

triggerProducer = cms.EDProducer('TriggerProducer',
trigTagArg1  = cms.string('TriggerResults'),
trigTagArg2  = cms.string(''),
trigTagArg3  = cms.string('HLT'),
prescaleTagArg1  = cms.string('patTrigger'),
prescaleTagArg2  = cms.string(''),
prescaleTagArg3  = cms.string(''),
VertexCollection  = cms.InputTag('offlineSlimmedPrimaryVertices'),
saveHLTObj = cms.bool(False),
trigObj = cms.InputTag('selectedPatTrigger'),
triggerNameList    =   cms.vstring()
)

from TreeMaker.TreeMaker.TMEras import TMeras
(TMeras.TM2017 | TMeras.TM2018).toModify(triggerProducer, trigObj = cms.InputTag("slimmedPatTrigger"))

