import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/00B030C1-BD42-E811-8FA6-0CC47A74527A.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/0AC7B455-A242-E811-A4F6-0CC47A7452DA.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/14B83B3B-9F42-E811-92A8-0025905A60B6.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/2EDCD3FE-AA42-E811-B7F8-7CD30AD09934.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/429925D7-C842-E811-A14F-24BE05C3B8B1.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/467A19F7-B142-E811-9E42-0025905C3DF6.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/4EA7073B-A542-E811-AC61-0025905A611E.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/624CB948-C842-E811-B201-0242AC130002.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/789FDEDD-B842-E811-9685-0025905C54D8.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/7CF1AC1C-BF42-E811-9407-0CC47A7C35C8.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/822941DD-B842-E811-8A33-0025905D1E08.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/82EAAB3D-C842-E811-98D6-0CC47A7C3444.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/8A9BD9C9-A042-E811-9D9D-7845C4FC35C9.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/9C0F47DE-B642-E811-923C-0025905A613C.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/A0ECD920-BA42-E811-A012-0CC47A4C8F18.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/AA0DA9E6-B842-E811-AB55-0025905A6118.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/ACD71184-C842-E811-9AAB-008CFAC941F0.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/CE299232-A842-E811-8F57-0025905B856C.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/E8DE8E2A-A842-E811-8966-7CD30AD0A15C.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/EEFFFB52-C842-E811-9055-001E67580704.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/1A95C433-9F42-E811-81D9-0025905A60C6.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/1AD76812-A342-E811-9821-0025905A60C6.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/26A86888-A542-E811-B3AD-0CC47A4D760A.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/3A10D2EA-EA41-E811-933F-002590DD7E50.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/42088595-AF42-E811-8CBD-0025905B85FE.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/4248F423-2341-E811-8DEC-0CC47A4C8ECE.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/4668D3E6-A142-E811-80D5-0CC47A78A478.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/588688DC-AD42-E811-A8A8-0CC47A4C8E64.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/5E5C1B93-4242-E811-ACDC-0CC47A4D7616.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/643EBDD0-B142-E811-B569-0025905A60F4.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/6C1DC9B0-ED42-E811-852A-7CD30AC03722.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/74E35EDF-9742-E811-8C1E-0CC47A4D76B6.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/76EEF027-E742-E811-9198-0CC47A4D7664.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/7A8216C9-9C42-E811-9C7D-0CC47A745284.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/840E1F9E-A642-E811-981D-0CC47A4D768C.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/8884B5DF-A442-E811-9A03-0025905A60A0.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/8A3F9003-EE42-E811-A07A-0025905B8606.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/8E0F6790-CF42-E811-BBD1-0CC47A7C3450.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/9AA45130-1E41-E811-A37F-0CC47A78A468.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/A4BA9464-C642-E811-A82F-0025905B85DA.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/AA3C0866-A142-E811-A0BA-0025905A48EC.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/BCF5C636-B042-E811-B816-0CC47A4C8EC8.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/BE9CDDA1-9E42-E811-A72F-0CC47A4D7658.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/C48B6CB0-9342-E811-B313-0CC47A4D769A.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/D285C357-9C42-E811-908A-0CC47A78A4B0.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/D8CCE1C9-F141-E811-8FB0-0CC47A7C360E.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/DC8B7124-A342-E811-937E-0025905A6118.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/E27EE77D-A842-E811-A627-0CC47A4D76C8.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/E40DFBFC-A742-E811-B611-0025905B85B6.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/E6AC68AF-9B42-E811-9648-0CC47A4D75F8.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/EE8D92D3-AA42-E811-B75C-0CC47A7C35E0.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/F017A6CF-A042-E811-BABB-0025905A60B0.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/06724557-0F42-E811-B554-FA163E68055F.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/06B6882C-D141-E811-A331-008CFAC94150.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/18342F3A-0A42-E811-A434-02163E012E16.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/28F02D5E-6B42-E811-ABCA-0242AC1C0502.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/2C572A02-0B42-E811-98C8-E0071B6C9DF0.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/32AB4789-D942-E811-955F-FA163E39B2A0.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/32FFC8D1-A742-E811-87F1-001EC94A8EF1.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/3E146CC8-0142-E811-8F02-0CC47A6C0758.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/42D53632-FE41-E811-BE0C-0242AC130002.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/4630B999-8C42-E811-BF98-0CC47A745250.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/487F8EB4-0A42-E811-9C5E-002590E7DEBE.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/4A586928-EA42-E811-8954-0026B927869F.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/4EF5760E-0345-E811-A948-0CC47A4D75F6.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/54CBA545-EE44-E811-B5B1-0CC47A4C8F10.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/5C5209D5-CD42-E811-B4B5-0CC47A7EEC56.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/5CDC80B4-BF42-E811-A935-EC0D9A82237E.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/5EB80B7F-7D42-E811-A662-0025905B858E.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/60B9FAA7-FE41-E811-A85A-0CC47AD98CEA.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/702000E9-0942-E811-85A8-E0071B7A9810.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/7090FA0E-0642-E811-914C-FA163E9240FC.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/8084E10B-0542-E811-A099-0CC47A3B03EE.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/80AA503D-9842-E811-B63A-F04DA274BB9C.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/8261E5F2-C142-E811-8A59-5065F3818281.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/84FCD964-1442-E811-999A-008CFAE45450.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/86D12A9E-FE41-E811-8411-FA163EB8644D.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/8898B21B-FE41-E811-A42B-0242AC130002.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/8CDF25E9-A842-E811-9817-0CC47AA53D98.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/8E97EE11-0D42-E811-A8C3-5065F3815281.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/9429CDBB-F141-E811-B87A-0242AC130002.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/96C7B80A-6742-E811-A05E-0242AC1C0500.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/98125E0C-4043-E811-BB90-24BE05CE6D61.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/983B9153-F841-E811-ABB4-0242AC130002.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/98A73F7D-FA41-E811-B1E3-A0369FD20730.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/9AECEEE9-1942-E811-915D-24BE05BDBE61.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/9CB3B163-6942-E811-8646-0242AC1C0502.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/9E134C17-EC41-E811-8DAC-0242AC130002.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/A2051730-FE41-E811-9F98-0242AC130002.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/A218E088-C842-E811-AF47-24BE05C44BB1.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/A4B0A5DC-CC44-E811-A09A-E0071B6C9DB0.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/AAC023DB-CB44-E811-B01C-0025905A60D2.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/ACBED69D-8042-E811-B54E-0025905C42A4.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/B0B586D8-3543-E811-A1F5-0242AC1C0500.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/B4F7633C-4043-E811-9168-801844E561F8.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/B6CE3667-0345-E811-9A89-90B11C0BDA0F.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/B6F721DF-C442-E811-BF1F-EC0D9A8225FE.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/C6B3377A-1142-E811-96A3-008CFAC9170C.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/C8BE155C-8042-E811-8C7D-0025905A6118.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/D4C4BF89-9142-E811-A369-44A84225CDFE.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/D67344EA-A042-E811-BA49-1CB72C0A3D89.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/DE6312EE-3F43-E811-B7B7-0CC47A7C3410.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/DEEEB4C6-4442-E811-9789-0CC47A5FC619.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/E6C08AF3-0D42-E811-A227-008CFAE453B8.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/E6C97653-8142-E811-83E7-0025905B85D0.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/EEC55216-F341-E811-A641-0242AC130002.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/F20191C9-EE41-E811-89F0-0242AC130002.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/F486BD19-0942-E811-8332-0CC47A3B02E6.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/F6A55B97-CE44-E811-8520-003048FFD76C.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/70000/FA6F3194-7B42-E811-ACFC-0025905C43EC.root',
       '/store/mc/RunIIFall17MiniAODv2/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/710000/1CA3BF10-BA44-E811-B9B6-002590E7D7E2.root',
] )