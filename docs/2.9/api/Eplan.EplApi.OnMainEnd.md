# Eplan.EplApi.OnMainEnd
Send when the Main End starts. 

  


#### Parameters

Has no event parameter.  


  
**Example**

```csharp
m_EventHandler = new EventHandler("Eplan.EplApi.OnMainEnd");
m_EventHandler.EplanEvent += delegate {
    new Decider().Decide(EnumDecisionType.eOkDecision, "On main end was called!", "OnMainEnd", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);
};
```
