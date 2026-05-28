import { useState, useRef } from 'react';
import api from '../services/api';
import './IntegrationTerminal.css';

function IntegrationTerminal() {
  const [expression, setExpression] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  
  const inputRef = useRef(null);

  const macros = [
    { label: 'sin', value: 'sin(' },
    { label: 'cos', value: 'cos(' },
    { label: 'tan', value: 'tan(' },
    { label: 'ln', value: 'ln(' },
    { label: 'exp', value: 'exp(' },
    { label: 'arcsin', value: 'arcsin(' },
    { label: 'π', value: 'pi' },
    { label: 'e', value: 'e' },
    { label: '^', value: '^' },
    { label: '*', value: '*' }
  ];

  const handleMacroClick = (macroValue) => {
    const input = inputRef.current;
    if (!input) return;

    const start = input.selectionStart;
    const end = input.selectionEnd;
    const currentText = expression;

    const newText = currentText.substring(0, start) + macroValue + currentText.substring(end);
    setExpression(newText);

    setTimeout(() => {
      input.focus();
      const newCursorPos = start + macroValue.length;
      input.setSelectionRange(newCursorPos, newCursorPos);
    }, 0);
  };

  const handleClear = () => {
    setExpression('');
    setResult(null);
    if (inputRef.current) inputRef.current.focus();
  };

  const handleSubmit = async (e) => {
    if (e) e.preventDefault();
    if (!expression.trim()) return;

    setLoading(true);
    setResult(null);

    try {
      const response = await api.post('/api/integrate', {
        expression: expression.trim()
      });
      setResult(response.data.integrated_result);
    } catch {
      setResult("Error: Communication with SAINT Core failed.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="integration-container">
      <form onSubmit={handleSubmit} className="integration-card">
        {/* Simplified Input Shell */}
        <div className="input-row">
          <input
            ref={inputRef}
            type="text"
            className="clean-math-input"
            value={expression}
            onChange={(e) => setExpression(e.target.value)}
            placeholder="Input the integrand as f(x)"
            autoFocus
          />
        </div>

        {/* Dynamic Macro Helper Deck */}
        <div className="macro-shelf">
          {macros.map((macro) => (
            <button
              key={macro.label}
              type="button"
              className="macro-btn"
              onClick={() => handleMacroClick(macro.value)}
            >
              {macro.label}
            </button>
          ))}
          <button type="button" className="macro-btn action-clear" onClick={handleClear}>
            Clear
          </button>
          <button type="submit" className="macro-btn action-run" disabled={loading}>
            {loading ? 'COMPUTING...' : 'RUN'}
          </button>
        </div>

        {/* Syntax Tooltip */}
        <div className="syntax-help">
          <strong>Syntax Guide:</strong> Use variables <code>x</code>, operators <code>+ - * / ^</code>, 
          and functions like <code>sin(x)</code>, <code>ln(x)</code>, <code>exp(x)</code>.
        </div>

        {/* Integrated Output Block */}
        {result && (
          <div className="output-display-block">
            <div className="output-label">// INTEGRATION RESULT:</div>
            <div className="output-text">{result}</div>
          </div>
        )}
      </form>
    </div>
  );
}

export default IntegrationTerminal;