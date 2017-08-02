import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/data/Run2017A/SinglePhoton/MINIAOD/PromptReco-v3/000/296/880/00000/A26931EC-3D55-E711-BDB7-02163E013865.root',
'/store/data/Run2017A/SinglePhoton/MINIAOD/PromptReco-v3/000/296/881/00000/7AA55A3E-4555-E711-82C5-02163E01341F.root',
'/store/data/Run2017A/SinglePhoton/MINIAOD/PromptReco-v3/000/296/887/00000/7AFFAE25-4B55-E711-AEFA-02163E0146E9.root',
'/store/data/Run2017A/SinglePhoton/MINIAOD/PromptReco-v3/000/296/888/00000/0007E710-9555-E711-AFAC-02163E014722.root',
'/store/data/Run2017A/SinglePhoton/MINIAOD/PromptReco-v3/000/296/888/00000/707282D6-8F55-E711-8BB3-02163E0146D5.root',
'/store/data/Run2017A/SinglePhoton/MINIAOD/PromptReco-v3/000/296/888/00000/AACBC586-8B55-E711-824A-02163E0125DF.root',
'/store/data/Run2017A/SinglePhoton/MINIAOD/PromptReco-v3/000/296/889/00000/70D757C4-9955-E711-B0D6-02163E0118D6.root',
'/store/data/Run2017A/SinglePhoton/MINIAOD/PromptReco-v3/000/296/895/00000/A28AA981-7D55-E711-B8EF-02163E012345.root',
'/store/data/Run2017A/SinglePhoton/MINIAOD/PromptReco-v3/000/296/897/00000/FEE3B268-A055-E711-AC4A-02163E01397E.root',
'/store/data/Run2017A/SinglePhoton/MINIAOD/PromptReco-v3/000/296/898/00000/7488EED3-A755-E711-A2C7-02163E011AEC.root',
'/store/data/Run2017A/SinglePhoton/MINIAOD/PromptReco-v3/000/296/899/00000/2E76AAEB-C255-E711-BDE2-02163E013987.root',
'/store/data/Run2017A/SinglePhoton/MINIAOD/PromptReco-v3/000/296/900/00000/F21E01C2-9255-E711-80BB-02163E0121AB.root',
'/store/data/Run2017A/SinglePhoton/MINIAOD/PromptReco-v3/000/296/903/00000/42D207B4-9B55-E711-9B92-02163E0135DE.root',
'/store/data/Run2017A/SinglePhoton/MINIAOD/PromptReco-v3/000/296/904/00000/E2E1F152-A455-E711-837A-02163E011A70.root',
'/store/data/Run2017A/SinglePhoton/MINIAOD/PromptReco-v3/000/296/966/00000/66D10317-C455-E711-9367-02163E014434.root',
'/store/data/Run2017A/SinglePhoton/MINIAOD/PromptReco-v3/000/296/966/00000/6CC96F69-B755-E711-89FE-02163E0122FC.root',
'/store/data/Run2017A/SinglePhoton/MINIAOD/PromptReco-v3/000/296/967/00000/80D0237C-BC55-E711-BE11-02163E013868.root',
'/store/data/Run2017A/SinglePhoton/MINIAOD/PromptReco-v3/000/296/968/00000/A252976A-BB55-E711-93CB-02163E011FEE.root',
'/store/data/Run2017A/SinglePhoton/MINIAOD/PromptReco-v3/000/296/969/00000/42BD1D2E-C655-E711-8121-02163E01375A.root',
'/store/data/Run2017A/SinglePhoton/MINIAOD/PromptReco-v3/000/296/970/00000/2678EFB0-DC55-E711-81F8-02163E013810.root',
'/store/data/Run2017A/SinglePhoton/MINIAOD/PromptReco-v3/000/296/970/00000/905F9F74-D155-E711-BABF-02163E0133F1.root',
'/store/data/Run2017A/SinglePhoton/MINIAOD/PromptReco-v3/000/296/971/00000/CA6B425C-CE55-E711-B0B4-02163E013550.root',
'/store/data/Run2017A/SinglePhoton/MINIAOD/PromptReco-v3/000/296/972/00000/5CC06A9A-F455-E711-9BBB-02163E0138D6.root',
'/store/data/Run2017A/SinglePhoton/MINIAOD/PromptReco-v3/000/296/972/00000/A8089764-DD55-E711-976A-02163E0144E0.root',
'/store/data/Run2017A/SinglePhoton/MINIAOD/PromptReco-v3/000/296/976/00000/0EDE525E-F155-E711-BBBE-02163E0141FC.root',
'/store/data/Run2017A/SinglePhoton/MINIAOD/PromptReco-v3/000/296/976/00000/E634F86F-DE55-E711-AFC0-02163E0145C4.root',
'/store/data/Run2017A/SinglePhoton/MINIAOD/PromptReco-v3/000/296/977/00000/60AD18B7-E355-E711-9750-02163E012086.root',
'/store/data/Run2017A/SinglePhoton/MINIAOD/PromptReco-v3/000/296/977/00000/7456AACE-FF55-E711-9DCD-02163E011807.root',
'/store/data/Run2017A/SinglePhoton/MINIAOD/PromptReco-v3/000/296/977/00000/B8E15EDE-EE55-E711-9B84-02163E01A2E1.root',
'/store/data/Run2017A/SinglePhoton/MINIAOD/PromptReco-v3/000/296/978/00000/DC52CC7B-0356-E711-8FB1-02163E0144B1.root',
'/store/data/Run2017A/SinglePhoton/MINIAOD/PromptReco-v3/000/296/979/00000/40462A0A-F755-E711-9537-02163E0141CE.root',
'/store/data/Run2017A/SinglePhoton/MINIAOD/PromptReco-v3/000/296/980/00000/9E4ADF50-2056-E711-AD72-02163E019E13.root',
'/store/data/Run2017A/SinglePhoton/MINIAOD/PromptReco-v3/000/297/003/00000/E4814CD2-1856-E711-9B65-02163E011EC8.root',
'/store/data/Run2017A/SinglePhoton/MINIAOD/PromptReco-v3/000/297/004/00000/9E500AE1-2C56-E711-BE82-02163E019D03.root' ] );
