# 🔗 MCP Global Hub Connection

## 📡 N8N MCP Server Connection

**Локация MCP сервера:** `C:\Users\79818\Desktop\MCP Global\mcp-servers\n8n-mcp`

### 🚀 Быстрый запуск MCP управления

```bash
# Переход к MCP серверу
cd "C:\Users\79818\Desktop\MCP Global\mcp-servers\n8n-mcp\_technical"

# Установка (если не установлено)
npm install

# Активация профиля N8N
npm run setup n8n

# Запуск Claude Code с N8N MCP
claude
```

### ⚡ Команды управления workflow'ами

После запуска Claude с MCP доступны команды:

```bash
# Список всех workflow'ов
"Покажи все N8N workflow'ы"

# Статус конкретного workflow'а  
"Статус workflow 'B2B Sales Proposal Automation'"

# Запуск workflow'а
"Запусти workflow '2.0 Automate Personalized Upwork Proposals'"

# История выполнений
"Покажи последние 5 выполнений workflow"

# Активация workflow'а
"Активируй workflow 'B2B Sales Proposal Automation'"
```

## 🎛️ MCP Server конфигурация

### Текущие настройки:
- **N8N Cloud URL:** `https://leonidshvorob.app.n8n.cloud`
- **API доступ:** ✅ Настроен
- **Статус подключения:** ✅ Работает  
- **Найдено workflow'ов:** 31 (7 Upwork)

### Проверка статуса MCP:
```bash
# Тест подключения
cd "C:\Users\79818\Desktop\MCP Global\mcp-servers\n8n-mcp\tools"
python test-connection.py
```

## 📋 Workflow Management через MCP

### Приоритетные действия:

1. **Активировать Tier 1 workflows:**
   - B2B Sales Proposal Automation (18 nodes)
   - 2.0 Automate Personalized Upwork Proposals (8 nodes)

2. **Настроить мониторинг:**
   - Real-time статус через MCP
   - Логи выполнений
   - Error tracking

3. **Оптимизировать workflow'ы:**
   - Объединить дублирующиеся
   - Улучшить integration points
   - Добавить fallback механизмы

## 🔄 Sync Strategy

**Идея:** Не копировать MCP сервер, а использовать как remote service

**Преимущества:**
- ✅ Единый источник правды
- ✅ Автоматические обновления MCP Global Hub
- ✅ Централизованная конфигурация
- ✅ Shared между проектами

**Недостатки:**
- ⚠️ Зависимость от MCP Global Hub
- ⚠️ Нужно запускать из другой папки

**Решение:** Создать wrapper скрипты в этой папке для удобства

---

**🔗 Связь с MCP Global Hub поддерживается**  
**📊 Статус:** Готов к использованию  
**🎯 Цель:** Единая точка управления всеми N8N автоматизациями