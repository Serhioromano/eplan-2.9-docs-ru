# Eplan.EplApi.OnPostOpenProject

Project management: After opening a project 

  


#### Parameters

Parameter Type: AfEvParString  
Parameter Description: Name of project which is opened.  


  
Example
    
    
    m_EventHandler = new EventHandler("Eplan.EplApi.OnPostOpenProject");
    m_EventHandler.EplanEvent += delegate(IEventParameter parameter)
    {
        new Decider().Decide(EnumDecisionType.eOkDecision, " Project " + new EventParameterString(parameter).String + " was open!", "OnPostOpenProject", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);
    };
