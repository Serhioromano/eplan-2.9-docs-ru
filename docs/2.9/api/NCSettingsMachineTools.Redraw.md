# NCSettingsMachineTools.Redraw

Force a Redraw for the NC Machine Tools settings tab 

  


  
Example
    
    
    m_EventHandler = new EventHandler("NCSettingsMachineTools.Redraw");
    m_EventHandler.EplanEvent += delegate {
        new Decider().Decide(EnumDecisionType.eOkDecision, "NCSettingsMachineTools.Redraw was called!", "", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);
    };
