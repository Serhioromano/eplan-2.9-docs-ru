# Операция: XDLInsertDeviceAction

**Параметр** |  **Описание**
---|---
PartNr  |  Номер изделия
PartVariant  |  Вариант изделия
ProjectId  |  Идентификатор проекта
PropertyIndex  |  Индекс покупных изделий ограничен значениями: 1–50. Если PropertyIndex = 0, покупное изделие не установлено.

!!! example "Пример:"

    XDLInsertDeviceAction
    /PartNr:MOE.010042
    /PartVariant:1
    /PropertyIndex:0
    /ProjectId:0
