# Eplan.EplApi.OnUserPreCloseProject
Project management: Before closing a project 

  


#### Parameters

Parameter Type: AfEvParString  
Parameter Description: Name of project which will be closed.  


  
**Example**

```csharp
m_EventHandler = new EventHandler("Eplan.EplApi.OnUserPreCloseProject");
m_EventHandler.EplanEvent += delegate (IEventParameter parameter)
{
    new Decider().Decide(EnumDecisionType.eOkDecision, " Project " + new EventParameterString(parameter).String + " will be closed!", "OnUserPreCloseProject", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);
};
```
