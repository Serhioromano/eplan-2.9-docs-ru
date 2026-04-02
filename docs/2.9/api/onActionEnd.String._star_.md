# `onActionEnd.String`.*

Send after the end of any Action.

 

 

**Example**

```csharp
m_EventHandler = new EventHandler("onActionEnd.String.*");
m_EventHandler.EplanEvent += delegate (IEventParameter parameter)
{
    new Decider().Decide(EnumDecisionType.eOkDecision, " Action " + new EventParameterString(parameter).String + " was called!", "", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);
};



m_EventHandler = new EventHandler("onActionEnd.String.XPartsManagementStart");
m_EventHandler.EplanNameEvent += delegate

{
    new Decider().Decide(EnumDecisionType.eOkDecision, " Action XPartsManagementStart was be called!", "", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);
};
```
