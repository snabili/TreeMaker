import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/04E0558A-1442-E811-930D-0CC47AF9B1AE.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/04EDBCEE-7742-E811-B02C-0025905C2CE8.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/08EC4092-8E42-E811-A8D2-0025905C53DC.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/0A6150BE-6D42-E811-A4C5-0CC47AF9B306.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/0AB9F074-7842-E811-A877-0025905C4262.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/1296DDB1-8742-E811-95E6-0025904C6566.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/166D4973-7F42-E811-8CAD-0025905BA734.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/18EB969A-8042-E811-94A9-0025904C637C.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/1EB0F73D-5C42-E811-8EF3-0025905D1E0A.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/2202CB07-7D42-E811-892F-0025904C66E6.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/22242687-8542-E811-85EB-0025905C53F0.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/243801C3-F441-E811-89FA-0025905C54DA.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/24A0CC9F-7542-E811-B466-0025905C53A8.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/285F6B9A-6E42-E811-AEB3-0025904C4E2A.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/2887387A-8F42-E811-ABA8-0025905C431A.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/28AA0A92-5542-E811-AED1-0025904CF764.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/2A9DDE03-6B42-E811-BA6C-0025905BA736.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/2AE59B08-9342-E811-9CFD-0CC47AF9B2B6.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/30982D57-8642-E811-9029-0025905C431A.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/30FC8222-0242-E811-A644-0CC47AF9B1D2.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/32351684-5E42-E811-823A-0025904C5DE0.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/34CFD305-6A42-E811-9BAB-0025905C53DE.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/36256286-8542-E811-B963-0025905C42A8.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/36C17D6F-8042-E811-955E-0025905C4264.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/36E263BC-6D42-E811-AFA7-0CC47AF9B1DE.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/42D6F30A-8A42-E811-AD59-0025905D1CB2.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/44E995FC-9042-E811-983C-0CC47AF9B2B6.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/464FFA43-8C42-E811-A676-0025905C2CD0.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/52FF9F14-0042-E811-9F72-0025904C51FC.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/56A78743-2942-E811-9ED8-0025905C96EA.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/5ABEE84B-5E42-E811-9CBA-0025905D1E0A.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/5CD88619-7C42-E811-98FF-0025905C2CA6.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/5E81008D-6B42-E811-B9DA-0025905C54B8.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/62BA7363-6C42-E811-B681-0025905C2CE6.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/66358D43-2642-E811-9772-0025905D1CB6.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/6A1BFBBD-9942-E811-9128-842B2B76653D.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/6CAABBB8-7A42-E811-B846-0025904C66E6.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/728F1F9C-7542-E811-855A-0CC47AF9B496.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/7488DBBA-6D42-E811-B5B0-0025904C540C.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/76F3F90B-6442-E811-A30E-0025905C3E68.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/7890A38E-6142-E811-A64A-0025905C2CEA.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/78EA3409-8342-E811-B0CF-0025905D1CB2.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/7C427210-9742-E811-8020-0025904C66E6.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/7C574B0F-6942-E811-A7BB-0025905BA736.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/801A212B-2442-E811-8819-0025904C637A.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/844557EA-7742-E811-95EC-0025904CF766.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/845E6536-0A42-E811-8632-0025905D1CB0.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/866F6629-5D42-E811-B3EA-0025905BA734.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/880CFB08-7742-E811-B768-0025905C3DF8.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/8A749E4D-0C42-E811-9E78-0025904C51FC.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/9224FD56-7342-E811-9A2D-0025905C2CB8.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/94018C2B-FF41-E811-AD24-0025905C3D6A.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/94F876B8-6742-E811-97E3-0025905C4300.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/98BBC05D-6642-E811-A028-0025905BA736.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/9CF5CCB8-7A42-E811-AC8A-0025905C3DD0.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/A0057767-5942-E811-A3EA-0025905C42F2.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/A095C1F9-7D42-E811-8BA5-0025904C637C.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/A61AC627-7042-E811-BE69-0025904E9012.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/A83CE69A-FA41-E811-9D2E-0CC47AF9B2B6.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/AA6B0BA1-7A42-E811-BF8E-0025904CF766.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/B4285C26-1A42-E811-8FD5-0025905C96EA.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/B47BA494-7442-E811-A5E2-0025904CF766.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/B87FCDFD-7042-E811-832B-0CC47AF9B306.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/BAAE6EC0-2742-E811-AA95-0025905C2CB8.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/BADC3150-0142-E811-81C1-0025905C43EC.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/BC2AFF64-6042-E811-B8AB-0025904C5DE0.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/C0298AC7-8D42-E811-8686-0025904C66A4.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/C0A11FF7-6442-E811-925F-0025905D1CB2.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/C88AB81B-8942-E811-BFD9-0025905C3D98.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/C8E70F56-2242-E811-B68C-0025904C637A.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/CCFC4568-7F42-E811-9FD5-0025904C66E6.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/D2AB8277-7E42-E811-B71F-0025905C3DD6.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/D6C2DF38-6342-E811-A432-0025905C2CB8.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/D6D20FC2-9942-E811-9A68-0025904C540E.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/D86D8494-7442-E811-BC71-0025904C66E6.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/D893B04A-2642-E811-A5CE-0CC47AF9B496.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/D8DF34D4-7142-E811-852F-0025905C2CB8.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/DA4C1807-8342-E811-A865-0025904C66A6.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/DCF4CE27-7042-E811-9D1E-0025905D1E00.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/DE32A3A3-0342-E811-A766-0CC47AF9B306.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/E208C327-7642-E811-BB19-0025905D1D02.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/E438EE47-1C42-E811-8B29-0025904CF100.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/E499E974-6F42-E811-BE25-0025904CF102.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/E6001F81-7942-E811-A71B-0025904C540C.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/E64D1C94-7B42-E811-A7F1-0CC47AF9B2E6.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/ECE4E2C8-2942-E811-8EBA-0025905C5484.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/F0D7F5B7-6742-E811-91BE-0025904C6622.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/F283A479-8F42-E811-AF64-0025905D1E08.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/F4904107-6A42-E811-81BF-0025905C3D40.root',
       '/store/mc/RunIIFall17MiniAODv2/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/40000/F69A63D0-5942-E811-A63D-0025905C2C86.root',
] )