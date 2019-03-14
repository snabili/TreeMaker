import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/00212EBC-85ED-E811-A454-0025905B857C.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/009084B2-9CED-E811-A4C7-0CC47A7C357E.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/00CA54F7-D4ED-E811-9B4B-0CC47A7C35D8.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/043F1983-69EF-E811-8562-0025905A60FE.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/04AD1C51-8EEF-E811-9DC4-0CC47A7C3434.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/0613D71A-7FEF-E811-A7C6-0CC47A7C3572.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/06C3E024-6FF0-E811-91E2-0CC47A4D76B2.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/06EEF0E2-91ED-E811-9B26-0CC47A4D760A.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/0A7AF4CB-90EF-E811-A8DB-0CC47A4D7614.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/0A9D8E7B-6AEF-E811-9209-0CC47A7C346E.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/0E06F2A4-8BED-E811-B465-003048FFD772.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/103B82FB-B3ED-E811-8B16-0CC47A4C8F30.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/10E2C311-81EF-E811-B6ED-0CC47A7C360E.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/120283B2-83ED-E811-A320-0CC47A4C8EE8.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/1472AF52-CAEF-E811-9679-0025905B8598.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/14F75507-C7EF-E811-B117-0CC47A7C346E.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/16613F1B-68EF-E811-8B16-0025905A60DA.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/1E148B55-90EF-E811-A553-0CC47A4C8F2C.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/1E8E4FB8-87ED-E811-89C4-0CC47A7C34E6.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/1E9D10E3-8CED-E811-B737-0CC47A4C8E3C.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/22421EC4-7AEF-E811-88DC-0CC47A4D762E.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/2A168B91-F5EF-E811-8C8E-0CC47A4C8E14.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/2AA0875E-8EEF-E811-8021-0025905A6082.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/2CFB6CFD-8BED-E811-95E3-0CC47A4D75F0.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/2E8BFDB6-87ED-E811-A245-0CC47A74527A.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/2EDF95C6-E3EF-E811-86F6-0025905A605E.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/2EE5DFD1-6FEF-E811-88ED-0CC47A4D7606.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/32037864-84ED-E811-BEA6-002618FDA265.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/365EA24B-8FEF-E811-BAEC-0025905A48F0.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/384BD577-DCEF-E811-A00C-0025905B8574.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/3A731F03-8AED-E811-94E3-0025905A6134.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/3A8444D8-72EF-E811-A3E7-0CC47A4C8F1C.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/3A9E4B60-B0EF-E811-97FF-0CC47A7C3412.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/3AB12DBF-D4EF-E811-BC9E-0025905A60B8.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/407EB946-0EEE-E811-A83C-0025905A60B6.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/461977F8-8AED-E811-B5D0-0CC47A4D764A.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/483AD4BD-EDEF-E811-BAA3-0CC47A78A468.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/48403E73-FAEF-E811-855C-0CC47A4C8E1C.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/48B2F6C7-D0EF-E811-ACA1-0CC47A78A3F8.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/4AEECB92-7AEF-E811-A715-0CC47A7C3430.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/4AFD40A9-CDED-E811-9455-0CC47A7C3412.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/4C42DB29-79EF-E811-8BFE-0CC47A78A3F8.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/50495E3C-00F0-E811-B565-0CC47A4D7658.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/52780ADD-8EED-E811-9BA4-0CC47A7C3434.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/5459D06E-6BEF-E811-9382-0CC47A7C3450.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/58FA10F4-EBEF-E811-A4EF-0CC47A4D762A.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/5A774485-8CED-E811-A991-0025905A60BC.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/5ACEE1C6-83ED-E811-842D-0CC47A78A340.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/5C47F28D-81ED-E811-8C1E-0CC47A78A3E8.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/5E1C4512-6DEF-E811-A17A-0CC47A4C8F1C.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/60957D9F-86EF-E811-A1FB-0025905A6080.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/622C720A-C5EF-E811-8FA8-0025905AA9F0.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/6256490B-69EF-E811-BC77-0CC47A78A3F8.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/6413A3F7-83ED-E811-869F-0CC47A78A3F8.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/646A2EB9-83EF-E811-9D59-0CC47A7C357A.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/661DE036-90EF-E811-AC78-0CC47A7C361E.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/66F8CD63-7CEF-E811-BDFF-0CC47A7C3628.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/684EF21D-7FED-E811-BAA1-0CC47A4D7630.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/68F3548D-CEEF-E811-805C-0CC47A4D7618.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/68FBD1AF-83ED-E811-9BF6-0CC47A4D75EC.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/6A75FDDC-DEEF-E811-9F0C-0025905B8606.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/6CB97ED4-89EF-E811-9822-0025905A6080.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/729D1C3F-79EF-E811-AD19-0CC47A7C3458.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/74C1225E-A3ED-E811-9294-0025905A610C.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/76A911D2-68EF-E811-9F21-0CC47A4C8EE8.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/78C055CC-66EF-E811-88A1-0CC47A7C351E.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/7AB95BE8-8CED-E811-B995-0CC47A7C3610.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/7C707351-8FED-E811-94E9-0CC47A7C3444.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/7CC33FA8-E9EF-E811-ADC0-0CC47A78A3D8.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/7E05C2D7-D5EF-E811-B8BB-0025905A611C.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/7EAA0CDC-84ED-E811-A555-0CC47A4C8F06.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/829DF29A-89ED-E811-86DA-0CC47A78A436.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/860EF70D-7FED-E811-80BF-0CC47A7C3628.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/866B1433-80ED-E811-8FA3-0025905A60FE.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/8A3DA1EA-83ED-E811-B1DC-0CC47A4C8EBA.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/8AF87761-A3ED-E811-941A-0025905B8612.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/8CA8690C-82ED-E811-90A4-0CC47A4D7626.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/8E70EBA3-B7ED-E811-BD9A-0CC47A4C8E70.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/90D6FC2B-8EED-E811-A07D-0CC47A4C8E82.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/98F228A2-1FF0-E811-886E-0CC47A4C8EE8.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/9C56CC79-8FED-E811-A1AF-0025905A60D0.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/9CC0AC15-84EF-E811-AC13-0CC47A4C8E2E.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/9E7FCD6A-90ED-E811-BE5C-0CC47A4C8E38.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/9EAB170F-99ED-E811-98C1-0025905B860C.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/A09E525E-9AEF-E811-BB79-0CC47A4D768E.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/A241D266-8DED-E811-B3C0-0CC47A78A414.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/A2671411-E2EF-E811-92ED-0025905A6066.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/A4BD3203-C5EF-E811-8EDC-0CC47A7C3420.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/A4E7A196-90ED-E811-AC4C-003048FFCC16.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/A62D6216-8BED-E811-BDDF-0CC47A4C8F06.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/A6AB44C5-8AED-E811-89A1-0025905B8566.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/A6C86D3B-68EF-E811-A9CA-0025905A60B8.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/A84BA089-91ED-E811-91FE-0025905B85F6.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/A8A881A1-81ED-E811-BA5D-0CC47A4C8F18.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/A8AD3AEB-83ED-E811-B04A-0CC47A4C8F0C.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/AA4F2283-83ED-E811-A686-0CC47A7C346E.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/AC03CFE2-89ED-E811-8A94-0CC47A7C34C4.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/ACD9E2ED-8DEF-E811-89D1-0025905A6066.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/AED1777B-C3ED-E811-8A33-003048FFCBB2.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/B43ABA05-BDEF-E811-9EF1-0CC47A78A446.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/B4D1E784-8DEF-E811-9308-0CC47A4C8EC8.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/B659CFFE-85ED-E811-8CAE-0CC47A78A414.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/B8ACE86D-E7EF-E811-B46B-0025905B85D6.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/BA5B4B34-8BEF-E811-8684-0CC47A4D769E.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/BA7F99EE-88ED-E811-B49A-0CC47A7C340E.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/BA82F3FA-83ED-E811-84B6-0CC47A4C8F30.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/BAA58DB9-ADED-E811-9636-0CC47A7C3404.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/BC0130F7-A6ED-E811-B558-0CC47A4C8E96.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/BEFF9D7A-BFED-E811-8F08-0CC47A78A408.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/C21102B4-93ED-E811-BDBD-0025905A6068.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/C4119D80-7FED-E811-AFE7-0CC47A4D7674.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/C626DB47-9AED-E811-BF34-0CC47A4C8E46.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/C645ABEF-85ED-E811-A965-0CC47A78A468.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/C6727016-81ED-E811-AE7C-0CC47A78A360.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/C87D828F-73EF-E811-B6B6-0CC47A7C354A.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/CA5BE134-6CEF-E811-8501-0025905AA9CC.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/CC75374C-8FED-E811-B448-0CC47A7C3432.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/CE1AAF89-86EF-E811-9F3C-0025905B856C.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/D40597B4-6EEF-E811-A1B6-0CC47A78A41C.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/D634094D-88EF-E811-9BF9-0025905A60F4.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/DC0AAAAC-80ED-E811-B314-0CC47A4D7664.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/DE3D9353-8EED-E811-92DF-0CC47A7C354C.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/DE974461-89ED-E811-8EB2-0CC47A7C360E.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/E07379FC-88EF-E811-88AE-0CC47A7C340C.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/E0C2929E-97EF-E811-945E-0CC47A7C34B0.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/E253E6CC-6EEF-E811-B6E1-0CC47A4D764C.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/E6B80E85-81ED-E811-A759-0CC47A4C8EE2.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/E6C2C83A-E2EF-E811-AC2B-0025905B8568.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/E85FA2AB-B9ED-E811-BE77-0025905B8582.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/F22192BF-BFEF-E811-A7B3-0CC47A4C8F1C.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/F2302FF7-A6ED-E811-BA39-0CC47A4C8E96.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/F431F6CF-81ED-E811-B0D8-0CC47A4D75EE.root',
       '/store/mc/RunIISummer16MiniAODv3/TTJets_SingleLeptFromTbar_genMET-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/00000/F4976371-8AED-E811-9C72-0025905A6118.root',
] )