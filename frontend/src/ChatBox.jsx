import React, { useState, useEffect, useRef } from 'react';

export default function ChatBox() {
  const [messages, setMessages] = useState([]);
  const [prompt, setPrompt] = useState('');
  const [loading, setLoading] = useState(false);
  const endRef = useRef(null);

  const sendMessage = async () => {
    if (!prompt.trim()) return;
    const newMessages = [...messages, { role: 'user', content: prompt }];
    setMessages(newMessages);
    setPrompt('');
    setLoading(true);

    try {
      const res = await fetch('http://127.0.0.1:8000/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ prompt }),
      });
      const data = await res.json();
      setMessages([...newMessages, { role: 'assistant', content: data.response }]);
    } catch (e) {
      setMessages([...newMessages, { role: 'assistant', content: '❌ Ошибка ответа от сервера' }]);
    } finally {
      setLoading(false);
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  };

  useEffect(() => {
    endRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  return (
    <div className="flex flex-col h-screen max-w-3xl mx-auto p-4">
      <div className="flex-1 overflow-y-auto space-y-2 mb-4 bg-white rounded-xl p-4 shadow-inner">
        {messages.map((msg, idx) => (
          <div
            key={idx}
            className={`whitespace-pre-wrap p-3 rounded-xl ${
              msg.role === 'user'
                ? 'bg-blue-100 text-right self-end'
                : 'bg-gray-100 text-left self-start'
            }`}
          >
            <span className="text-sm text-gray-600 block">{msg.role === 'user' ? 'Вы' : 'ИИ'}</span>
            <span>{msg.content}</span>
          </div>
        ))}
        {loading && <div className="italic text-gray-400">ИИ печатает...</div>}
        <div ref={endRef} />
      </div>

      <textarea
        rows={2}
        className="w-full border rounded-xl p-3 shadow resize-none"
        placeholder="Напишите сообщение и нажмите Enter..."
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        onKeyDown={handleKeyDown}
      />
    </div>
  );
}
