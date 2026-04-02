# RefreshPageFilter

Page filter has been changed, refresh navigator data

 

 

**Example**

```csharp
m_EventHandler = new EventHandler("RefreshPageFilter");
m_EventHandler.EplanEvent += delegate {
    new Decider().Decide(EnumDecisionType.eOkDecision, "RefreshPageFilter was called!", "", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);
};
```
