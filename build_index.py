# -*- coding: utf-8 -*-
"""
Builder script to generate the complete, production-ready, standalone 'index.html'
for 'Simulasi Ujian Perangkat Desa - Kabupaten Tuban & Standar Nasional'.
Incorporates all 12 Mandatory Enhanced Features:
1. Realistic CAT Mode (prominent flag/ragu-ragu, question palette with status filters, pre-finish modal summary)
2. Weakness Analysis & Learning Recommendations (category scoring ranking, mastery grading, specific regulatory suggestions)
3. Simple Adaptive Drill (drill wrong answers, empty questions, flagged questions, category drills)
4. Village Governance Glossary (36 verified terms with instant search and category filters)
5. Score Progress & SVG Chart (visual trend chart, apple-to-apple session comparison with disparity notices)
6. Safe Randomization (switches for question shuffling and option shuffling with synchronized answer keys)
7. Verified Regulatory References (verified badges, legal basis, EYD V, math/logic notes)
8. Local Backup (export and import JSON with strict size, schema, and sanitization validation)
9. Accessibility (keyboard navigation A-D, arrows, R, P, Esc, visual focus rings, font size switcher A-/A/A+)
10. 100% Privacy & Offline (zero network calls, zero external trackers/CDNs)
11. Application Resilience (safe localStorage wrappers, corrupted JSON handling, refresh session recovery)
12. Comprehensive Testing Suite Ready
"""

import json
import os
from merge_and_validate import ALL_QUESTIONS
from glossary_data import GLOSSARY_TERMS

def build_standalone_index():
    questions_json = json.dumps(ALL_QUESTIONS, ensure_ascii=False)
    glossary_json = json.dumps(GLOSSARY_TERMS, ensure_ascii=False)

    html_content = f'''<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Simulasi Ujian Perangkat Desa | CBT Mandiri & Latihan Resmi</title>
  <meta name="description" content="Aplikasi simulasi ujian perangkat desa lengkap dan profesional berbasis CBT untuk persiapan seleksi perangkat desa Kabupaten Tuban dan standar nasional. Database 500 soal, acak 100 soal otomatis tanpa kecurangan, pilihan jawaban acak, glosarium desa, analisis kelemahan, dan riwayat nilai.">
  <meta name="author" content="Simulasi CBT Perangkat Desa">
  <style>
    /* ==========================================================================
       DESIGN SYSTEM & CSS VARIABLES
       Civic Navy & Emerald/Gold Theme - Clean, Authoritative, CBT Native
       ========================================================================== */
    :root {{
      --primary-900: #0a192f;
      --primary-800: #0f2b48;
      --primary-700: #1e3a8a;
      --primary-600: #2563eb;
      --primary-500: #3b82f6;
      --primary-100: #dbeafe;
      --primary-50:  #eff6ff;
      
      --accent-gold-700: #b45309;
      --accent-gold-600: #d97706;
      --accent-gold-500: #f59e0b;
      --accent-gold-100: #fef3c7;
      --accent-gold-50:  #fffbeb;
      
      --emerald-800: #065f46;
      --emerald-700: #047857;
      --emerald-600: #059669;
      --emerald-500: #10b981;
      --emerald-100: #d1fae5;
      --emerald-50:  #ecfdf5;
      
      --rose-700: #b91c1c;
      --rose-600: #dc2626;
      --rose-500: #ef4444;
      --rose-100: #fee2e2;
      --rose-50:  #fff1f2;
      
      --slate-900: #0f172a;
      --slate-800: #1e293b;
      --slate-700: #334155;
      --slate-600: #475569;
      --slate-500: #64748b;
      --slate-400: #94a3b8;
      --slate-300: #cbd5e1;
      --slate-200: #e2e8f0;
      --slate-100: #f1f5f9;
      --slate-50:  #f8fafc;
      
      --white: #ffffff;
      --font-main: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
      --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
      --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
      --shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
      --radius-sm: 6px;
      --radius-md: 10px;
      --radius-lg: 14px;
      --radius-full: 9999px;
      
      --app-font-scale: 100%;
    }}

    html {{
      font-size: var(--app-font-scale);
    }}

    *, *::before, *::after {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: var(--font-main);
      background-color: var(--slate-100);
      color: var(--slate-900);
      line-height: 1.5;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      -webkit-font-smoothing: antialiased;
    }}

    /* Accessibility Focus Ring (A11y) */
    :focus-visible {{
      outline: 3px solid var(--accent-gold-500);
      outline-offset: 2px;
    }}

    /* Civic Authority Header */
    .civic-header {{
      background: linear-gradient(135deg, var(--primary-900) 0%, var(--primary-800) 100%);
      color: var(--white);
      border-bottom: 3px solid var(--accent-gold-500);
      box-shadow: var(--shadow-md);
      position: sticky;
      top: 0;
      z-index: 1000;
    }}

    .header-container {{
      max-width: 1300px;
      margin: 0 auto;
      padding: 0.75rem 1.25rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
      flex-wrap: wrap;
    }}

    .brand-block {{
      display: flex;
      align-items: center;
      gap: 0.85rem;
      text-decoration: none;
      color: inherit;
      cursor: pointer;
    }}

    .brand-emblem {{
      width: 44px;
      height: 44px;
      background: linear-gradient(135deg, var(--accent-gold-500) 0%, var(--accent-gold-600) 100%);
      border-radius: var(--radius-md);
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--primary-900);
      box-shadow: 0 2px 4px rgba(0,0,0,0.2);
      flex-shrink: 0;
    }}

    .brand-title h1 {{
      font-size: 1.15rem;
      font-weight: 800;
      letter-spacing: 0.5px;
      line-height: 1.2;
      color: var(--white);
    }}

    .brand-title p {{
      font-size: 0.75rem;
      color: var(--slate-300);
      font-weight: 500;
    }}

    .header-nav {{
      display: flex;
      align-items: center;
      gap: 0.5rem;
      flex-wrap: wrap;
    }}

    .header-badge {{
      background: rgba(255, 255, 255, 0.12);
      border: 1px solid rgba(255, 255, 255, 0.2);
      color: var(--accent-gold-100);
      padding: 0.3rem 0.65rem;
      border-radius: var(--radius-full);
      font-size: 0.72rem;
      font-weight: 600;
      letter-spacing: 0.4px;
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
    }}

    .font-scale-control {{
      display: flex;
      align-items: center;
      background: rgba(0, 0, 0, 0.25);
      border: 1px solid rgba(255, 255, 255, 0.2);
      border-radius: var(--radius-sm);
      overflow: hidden;
    }}

    .font-scale-btn {{
      background: transparent;
      border: none;
      color: var(--white);
      padding: 0.3rem 0.55rem;
      font-size: 0.75rem;
      font-weight: 700;
      cursor: pointer;
      transition: background 0.15s;
    }}

    .font-scale-btn:hover {{
      background: rgba(255, 255, 255, 0.2);
    }}

    .font-scale-btn.active {{
      background: var(--accent-gold-500);
      color: var(--primary-900);
    }}

    /* Main Container */
    .app-main {{
      max-width: 1300px;
      width: 100%;
      margin: 0 auto;
      padding: 1.5rem 1.25rem 3rem;
      flex: 1;
    }}

    /* Alerts & Notifiers */
    .disclaimer-banner {{
      background-color: var(--slate-50);
      border-left: 4px solid var(--primary-600);
      padding: 0.75rem 1rem;
      border-radius: var(--radius-sm);
      margin-bottom: 1.5rem;
      font-size: 0.82rem;
      color: var(--slate-700);
      box-shadow: var(--shadow-sm);
      display: flex;
      align-items: flex-start;
      gap: 0.75rem;
    }}

    .resume-card {{
      background: var(--emerald-50);
      border: 1px solid var(--emerald-500);
      border-radius: var(--radius-md);
      padding: 1rem 1.25rem;
      margin-bottom: 1.5rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
      flex-wrap: wrap;
    }}

    /* Common Card */
    .cbt-card {{
      background: var(--white);
      border-radius: var(--radius-lg);
      border: 1px solid var(--slate-200);
      box-shadow: var(--shadow-sm);
      padding: 1.5rem;
      margin-bottom: 1.5rem;
    }}

    /* Hero Panel on Home */
    .hero-panel {{
      background: linear-gradient(135deg, var(--primary-900) 0%, var(--primary-700) 100%);
      color: var(--white);
      border-radius: var(--radius-lg);
      padding: 2.25rem 2rem;
      margin-bottom: 1.75rem;
      box-shadow: var(--shadow-lg);
      position: relative;
      overflow: hidden;
    }}

    .hero-panel::after {{
      content: "";
      position: absolute;
      right: -30px;
      bottom: -30px;
      width: 240px;
      height: 240px;
      background: radial-gradient(circle, rgba(245, 158, 11, 0.15) 0%, rgba(255,255,255,0) 70%);
      pointer-events: none;
    }}

    .hero-panel h2 {{
      font-size: 1.85rem;
      font-weight: 800;
      margin-bottom: 0.75rem;
      line-height: 1.25;
      letter-spacing: -0.3px;
    }}

    .hero-panel p.lead {{
      font-size: 1rem;
      color: var(--slate-200);
      max-width: 850px;
      margin-bottom: 1.5rem;
      line-height: 1.6;
    }}

    .hero-badge-row {{
      display: flex;
      gap: 0.65rem;
      flex-wrap: wrap;
      margin-bottom: 1.25rem;
    }}

    /* Badges */
    .badge-pill {{
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      padding: 0.25rem 0.65rem;
      border-radius: var(--radius-full);
      font-size: 0.75rem;
      font-weight: 700;
      line-height: 1;
    }}

    .badge-cat {{
      background: var(--primary-100);
      color: var(--primary-700);
      border: 1px solid rgba(30, 58, 138, 0.2);
    }}

    .badge-diff-mudah {{
      background: var(--emerald-100);
      color: var(--emerald-700);
      border: 1px solid rgba(4, 120, 87, 0.2);
    }}

    .badge-diff-sedang {{
      background: var(--accent-gold-100);
      color: var(--accent-gold-700);
      border: 1px solid rgba(180, 83, 9, 0.2);
    }}

    .badge-diff-sulit {{
      background: var(--rose-100);
      color: var(--rose-700);
      border: 1px solid rgba(185, 28, 28, 0.2);
    }}

    .badge-verified {{
      background: #e0f2fe;
      color: #0369a1;
      border: 1px solid #7dd3fc;
    }}

    /* Form & Input Groups */
    .form-candidate-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 1rem;
      background: rgba(255, 255, 255, 0.08);
      padding: 1.25rem;
      border-radius: var(--radius-md);
      border: 1px solid rgba(255, 255, 255, 0.15);
      margin-bottom: 1.5rem;
    }}

    .form-group label {{
      display: block;
      font-size: 0.82rem;
      font-weight: 600;
      color: var(--slate-200);
      margin-bottom: 0.35rem;
    }}

    .form-control {{
      width: 100%;
      padding: 0.65rem 0.85rem;
      border-radius: var(--radius-sm);
      border: 1px solid var(--slate-300);
      font-size: 0.92rem;
      font-family: inherit;
      color: var(--slate-900);
      background-color: var(--white);
      transition: border-color 0.15s, box-shadow 0.15s;
    }}

    .form-control:focus {{
      border-color: var(--primary-500);
      box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.2);
      outline: none;
    }}

    /* Switch toggles */
    .toggle-group {{
      display: flex;
      align-items: center;
      gap: 0.75rem;
      margin-top: 0.5rem;
    }}

    .toggle-switch {{
      position: relative;
      display: inline-block;
      width: 44px;
      height: 24px;
      flex-shrink: 0;
    }}

    .toggle-switch input {{
      opacity: 0;
      width: 0;
      height: 0;
    }}

    .toggle-slider {{
      position: absolute;
      cursor: pointer;
      top: 0; left: 0; right: 0; bottom: 0;
      background-color: var(--slate-400);
      transition: .2s;
      border-radius: 24px;
    }}

    .toggle-slider:before {{
      position: absolute;
      content: "";
      height: 18px;
      width: 18px;
      left: 3px;
      bottom: 3px;
      background-color: white;
      transition: .2s;
      border-radius: 50%;
    }}

    input:checked + .toggle-slider {{
      background-color: var(--emerald-600);
    }}

    input:checked + .toggle-slider:before {{
      transform: translateX(20px);
    }}

    /* Buttons */
    .btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 0.5rem;
      padding: 0.65rem 1.25rem;
      font-size: 0.92rem;
      font-weight: 700;
      border-radius: var(--radius-md);
      border: 1px solid transparent;
      cursor: pointer;
      transition: all 0.15s ease-in-out;
      text-decoration: none;
      line-height: 1.2;
    }}

    .btn:disabled {{
      opacity: 0.55;
      cursor: not-allowed;
    }}

    .btn-sm {{
      padding: 0.4rem 0.8rem;
      font-size: 0.82rem;
    }}

    .btn-lg {{
      padding: 0.85rem 1.65rem;
      font-size: 1.05rem;
    }}

    .btn-primary {{
      background: var(--primary-600);
      color: var(--white);
    }}
    .btn-primary:hover:not(:disabled) {{
      background: var(--primary-700);
      box-shadow: var(--shadow-md);
    }}

    .btn-gold {{
      background: linear-gradient(135deg, var(--accent-gold-500) 0%, var(--accent-gold-600) 100%);
      color: var(--primary-900);
      box-shadow: 0 2px 4px rgba(217, 119, 6, 0.3);
    }}
    .btn-gold:hover:not(:disabled) {{
      background: linear-gradient(135deg, var(--accent-gold-600) 0%, var(--accent-gold-700) 100%);
      color: var(--white);
    }}

    .btn-emerald {{
      background: var(--emerald-600);
      color: var(--white);
    }}
    .btn-emerald:hover:not(:disabled) {{
      background: var(--emerald-700);
    }}

    .btn-danger {{
      background: var(--rose-600);
      color: var(--white);
    }}
    .btn-danger:hover:not(:disabled) {{
      background: var(--rose-700);
    }}

    .btn-outline {{
      background: var(--white);
      border-color: var(--slate-300);
      color: var(--slate-700);
    }}
    .btn-outline:hover:not(:disabled) {{
      background: var(--slate-50);
      border-color: var(--slate-400);
      color: var(--slate-900);
    }}

    .btn-flagged {{
      background: var(--accent-gold-100) !important;
      border-color: var(--accent-gold-500) !important;
      color: var(--accent-gold-700) !important;
      font-weight: 800 !important;
    }}

    /* Action Cards Grid on Home */
    .actions-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 1.25rem;
      margin-bottom: 2rem;
    }}

    .action-card {{
      background: var(--white);
      border: 1px solid var(--slate-200);
      border-radius: var(--radius-lg);
      padding: 1.5rem;
      box-shadow: var(--shadow-sm);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: transform 0.2s, box-shadow 0.2s;
    }}

    .action-card:hover {{
      transform: translateY(-2px);
      box-shadow: var(--shadow-md);
      border-color: var(--primary-500);
    }}

    .action-card-header {{
      display: flex;
      align-items: center;
      gap: 0.85rem;
      margin-bottom: 0.75rem;
    }}

    .action-card-icon {{
      width: 42px;
      height: 42px;
      border-radius: var(--radius-md);
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }}

    .action-card h3 {{
      font-size: 1.15rem;
      font-weight: 800;
      color: var(--primary-900);
    }}

    .action-card p {{
      font-size: 0.88rem;
      color: var(--slate-600);
      line-height: 1.5;
      margin-bottom: 1.25rem;
    }}

    /* Category Distribution Table */
    .table-container {{
      overflow-x: auto;
      margin-top: 1rem;
      border-radius: var(--radius-md);
      border: 1px solid var(--slate-200);
    }}

    .cbt-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.88rem;
      background: var(--white);
      text-align: left;
    }}

    .cbt-table th {{
      background: var(--slate-100);
      color: var(--slate-800);
      font-weight: 700;
      padding: 0.75rem 1rem;
      border-bottom: 2px solid var(--slate-200);
      white-space: nowrap;
    }}

    .cbt-table td {{
      padding: 0.75rem 1rem;
      border-bottom: 1px solid var(--slate-200);
      vertical-align: middle;
    }}

    .cbt-table tr:hover {{
      background: var(--slate-50);
    }}

    /* ==========================================================================
       EXAM VIEW & CAT LAYOUT (VIEW 3)
       ========================================================================== */
    .cbt-exam-layout {{
      display: grid;
      grid-template-columns: 1fr 340px;
      gap: 1.5rem;
      align-items: start;
    }}

    @media (max-width: 992px) {{
      .cbt-exam-layout {{
        grid-template-columns: 1fr;
      }}
    }}

    /* Exam Top Status Bar */
    .exam-top-bar {{
      background: var(--white);
      border: 1px solid var(--slate-200);
      border-radius: var(--radius-md);
      padding: 0.85rem 1.25rem;
      margin-bottom: 1.25rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
      flex-wrap: wrap;
      box-shadow: var(--shadow-sm);
    }}

    .candidate-info-chip {{
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }}

    .candidate-avatar {{
      width: 38px;
      height: 38px;
      border-radius: 50%;
      background: var(--primary-700);
      color: var(--white);
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 800;
      font-size: 0.95rem;
    }}

    .candidate-text h4 {{
      font-size: 0.95rem;
      font-weight: 800;
      color: var(--slate-900);
      line-height: 1.2;
    }}

    .candidate-text p {{
      font-size: 0.75rem;
      color: var(--slate-500);
    }}

    /* Dual Timers Widget */
    .timers-wrapper {{
      display: flex;
      align-items: center;
      gap: 0.85rem;
      flex-wrap: wrap;
    }}

    .timer-badge {{
      display: flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.5rem 0.9rem;
      border-radius: var(--radius-md);
      font-weight: 800;
      font-size: 1.05rem;
      letter-spacing: 0.5px;
      box-shadow: inset 0 1px 2px rgba(0,0,0,0.06);
    }}

    .timer-badge.total-timer {{
      background: var(--primary-900);
      color: var(--accent-gold-500);
      border: 1px solid var(--accent-gold-600);
    }}

    .timer-badge.total-timer.urgent {{
      background: var(--rose-700);
      color: var(--white);
      animation: pulseAlert 1s infinite alternate;
    }}

    .timer-badge.question-timer {{
      background: var(--slate-100);
      color: var(--slate-800);
      border: 1px solid var(--slate-300);
      font-size: 0.92rem;
    }}

    .timer-badge.question-timer.urgent {{
      background: var(--rose-100);
      color: var(--rose-700);
      border-color: var(--rose-400);
    }}

    @keyframes pulseAlert {{
      from {{ transform: scale(1); }}
      to {{ transform: scale(1.02); box-shadow: 0 0 10px rgba(220, 38, 38, 0.4); }}
    }}

    /* Question Main Card */
    .question-card {{
      background: var(--white);
      border: 1px solid var(--slate-200);
      border-radius: var(--radius-lg);
      padding: 1.75rem;
      box-shadow: var(--shadow-sm);
      min-height: 480px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}

    .question-meta-row {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 0.75rem;
      margin-bottom: 1.25rem;
      padding-bottom: 0.85rem;
      border-bottom: 1px solid var(--slate-200);
      flex-wrap: wrap;
    }}

    .question-number-badge {{
      font-size: 1.1rem;
      font-weight: 800;
      color: var(--primary-900);
    }}

    .badges-group {{
      display: flex;
      gap: 0.4rem;
      align-items: center;
      flex-wrap: wrap;
    }}

    .question-text {{
      font-size: 1.12rem;
      line-height: 1.65;
      color: var(--slate-900);
      font-weight: 600;
      margin-bottom: 1.5rem;
    }}

    /* Options List */
    .options-list {{
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
      margin-bottom: 1.5rem;
    }}

    .option-item {{
      display: flex;
      align-items: flex-start;
      gap: 0.85rem;
      padding: 0.85rem 1rem;
      border-radius: var(--radius-md);
      border: 2px solid var(--slate-200);
      background: var(--white);
      cursor: pointer;
      transition: all 0.15s ease-in-out;
      user-select: none;
    }}

    .option-item:hover {{
      border-color: var(--primary-500);
      background: var(--primary-50);
    }}

    .option-item.selected {{
      border-color: var(--primary-600);
      background: var(--primary-50);
      box-shadow: 0 0 0 1px var(--primary-600);
    }}

    .option-letter {{
      width: 32px;
      height: 32px;
      border-radius: 50%;
      background: var(--slate-100);
      color: var(--slate-700);
      border: 1px solid var(--slate-300);
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 800;
      font-size: 0.88rem;
      flex-shrink: 0;
      transition: all 0.15s;
    }}

    .option-item.selected .option-letter {{
      background: var(--primary-600);
      color: var(--white);
      border-color: var(--primary-600);
    }}

    .option-item.eval-correct {{
      border-color: var(--emerald-600);
      background: var(--emerald-50);
    }}

    .option-item.eval-correct .option-letter {{
      background: var(--emerald-600);
      color: var(--white);
      border-color: var(--emerald-600);
    }}

    .option-item.eval-wrong {{
      border-color: var(--rose-600);
      background: var(--rose-50);
    }}

    .option-item.eval-wrong .option-letter {{
      background: var(--rose-600);
      color: var(--white);
      border-color: var(--rose-600);
    }}

    .option-content {{
      font-size: 0.98rem;
      color: var(--slate-800);
      line-height: 1.5;
      padding-top: 2px;
      flex: 1;
    }}

    /* Action Nav Bar */
    .cbt-action-bar {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 0.75rem;
      padding-top: 1.25rem;
      border-top: 1px solid var(--slate-200);
      flex-wrap: wrap;
    }}

    .cbt-action-left, .cbt-action-right {{
      display: flex;
      align-items: center;
      gap: 0.65rem;
      flex-wrap: wrap;
    }}

    /* Palette Sidebar */
    .palette-card {{
      background: var(--white);
      border: 1px solid var(--slate-200);
      border-radius: var(--radius-lg);
      padding: 1.25rem;
      box-shadow: var(--shadow-sm);
      position: sticky;
      top: 80px;
    }}

    .palette-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 0.85rem;
    }}

    .palette-header h3 {{
      font-size: 1.05rem;
      font-weight: 800;
      color: var(--primary-900);
    }}

    .palette-filter-bar {{
      display: flex;
      gap: 0.35rem;
      margin-bottom: 0.85rem;
      flex-wrap: wrap;
    }}

    .palette-filter-btn {{
      background: var(--slate-100);
      border: 1px solid var(--slate-200);
      padding: 0.25rem 0.5rem;
      border-radius: var(--radius-sm);
      font-size: 0.72rem;
      font-weight: 700;
      color: var(--slate-600);
      cursor: pointer;
    }}

    .palette-filter-btn.active {{
      background: var(--primary-700);
      color: var(--white);
      border-color: var(--primary-700);
    }}

    .palette-legend {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 0.4rem;
      font-size: 0.72rem;
      color: var(--slate-600);
      background: var(--slate-50);
      padding: 0.65rem;
      border-radius: var(--radius-sm);
      margin-bottom: 1rem;
      border: 1px solid var(--slate-200);
    }}

    .legend-item {{
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }}

    .legend-dot {{
      width: 12px;
      height: 12px;
      border-radius: 3px;
      flex-shrink: 0;
    }}

    .grid-palette {{
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 0.45rem;
      max-height: 380px;
      overflow-y: auto;
      padding-right: 4px;
    }}

    .btn-palette-num {{
      height: 36px;
      border-radius: var(--radius-sm);
      border: 1px solid var(--slate-300);
      background: var(--white);
      font-weight: 800;
      font-size: 0.82rem;
      color: var(--slate-700);
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      position: relative;
      transition: all 0.15s;
    }}

    .btn-palette-num:hover {{
      border-color: var(--primary-500);
      transform: scale(1.05);
    }}

    .btn-palette-num.answered {{
      background: var(--emerald-600);
      color: var(--white);
      border-color: var(--emerald-700);
    }}

    .btn-palette-num.flagged {{
      background: var(--accent-gold-500) !important;
      color: var(--primary-900) !important;
      border-color: var(--accent-gold-600) !important;
      font-weight: 900;
    }}

    .btn-palette-num.answered.flagged {{
      background: linear-gradient(135deg, var(--emerald-600) 65%, var(--accent-gold-500) 65%) !important;
      color: var(--white) !important;
    }}

    .btn-palette-num.skipped {{
      background: var(--rose-50);
      border-color: var(--rose-300);
      color: var(--rose-700);
    }}

    .btn-palette-num.active {{
      outline: 2px solid var(--primary-600);
      outline-offset: 1px;
      font-weight: 900;
    }}

    /* Pre-Finish Modal Status Pills */
    .status-summary-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(130px, 1fr));
      gap: 0.75rem;
      margin: 1rem 0;
    }}

    .status-pill-box {{
      padding: 0.85rem;
      border-radius: var(--radius-md);
      text-align: center;
      border: 1px solid var(--slate-200);
    }}

    .status-pill-box.answered {{
      background: var(--emerald-50);
      border-color: var(--emerald-300);
      color: var(--emerald-800);
    }}

    .status-pill-box.flagged {{
      background: var(--accent-gold-50);
      border-color: var(--accent-gold-300);
      color: var(--accent-gold-800);
    }}

    .status-pill-box.empty {{
      background: var(--rose-50);
      border-color: var(--rose-300);
      color: var(--rose-800);
    }}

    .status-pill-num {{
      font-size: 1.6rem;
      font-weight: 900;
      line-height: 1;
      margin-bottom: 0.25rem;
    }}

    .status-pill-label {{
      font-size: 0.75rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}

    .clickable-nums-wrap {{
      display: flex;
      flex-wrap: wrap;
      gap: 0.35rem;
      max-height: 120px;
      overflow-y: auto;
      padding: 0.5rem;
      background: var(--slate-50);
      border-radius: var(--radius-sm);
      border: 1px solid var(--slate-200);
      margin-top: 0.5rem;
    }}

    .jump-chip {{
      padding: 0.2rem 0.55rem;
      border-radius: var(--radius-sm);
      font-size: 0.75rem;
      font-weight: 700;
      cursor: pointer;
      border: 1px solid var(--slate-300);
      background: var(--white);
    }}

    .jump-chip:hover {{
      background: var(--primary-100);
      border-color: var(--primary-600);
    }}

    /* ==========================================================================
       RESULTS & WEAKNESS ANALYSIS (VIEW 4)
       ========================================================================== */
    .results-hero {{
      background: linear-gradient(135deg, var(--primary-900) 0%, var(--primary-800) 100%);
      color: var(--white);
      border-radius: var(--radius-lg);
      padding: 2rem;
      margin-bottom: 1.75rem;
      box-shadow: var(--shadow-lg);
    }}

    .results-hero-grid {{
      display: grid;
      grid-template-columns: 1fr 280px;
      gap: 2rem;
      align-items: center;
    }}

    .results-score-badge {{
      background: rgba(255, 255, 255, 0.08);
      border: 2px solid var(--accent-gold-500);
      border-radius: var(--radius-lg);
      padding: 1.5rem;
      text-align: center;
      box-shadow: var(--shadow-md);
    }}

    .results-score-badge .score-value {{
      font-size: 3.5rem;
      font-weight: 900;
      color: var(--accent-gold-500);
      line-height: 1;
      margin: 0.35rem 0;
    }}

    .results-stats-row {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(110px, 1fr));
      gap: 0.75rem;
      margin-top: 1.25rem;
    }}

    .stat-box {{
      background: rgba(255, 255, 255, 0.1);
      border-radius: var(--radius-md);
      padding: 0.75rem;
      text-align: center;
    }}

    .stat-box-num {{
      font-size: 1.35rem;
      font-weight: 800;
    }}

    .stat-box-num.benar {{ color: var(--emerald-400); }}
    .stat-box-num.salah {{ color: var(--rose-400); }}
    .stat-box-num.kosong {{ color: var(--slate-300); }}

    /* Weakness Analysis Section */
    .weakness-card {{
      background: var(--white);
      border-radius: var(--radius-md);
      border: 1px solid var(--slate-200);
      padding: 1rem 1.25rem;
      margin-bottom: 0.85rem;
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
      transition: border-color 0.15s;
    }}

    .weakness-card.needs-work {{
      border-left: 5px solid var(--rose-600);
      background: #fffafa;
    }}

    .weakness-card.fair {{
      border-left: 5px solid var(--accent-gold-500);
    }}

    .weakness-card.mastered {{
      border-left: 5px solid var(--emerald-600);
    }}

    .weakness-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 0.5rem;
    }}

    .progress-bar-wrap {{
      width: 100%;
      height: 8px;
      background: var(--slate-200);
      border-radius: var(--radius-full);
      overflow: hidden;
      margin: 0.35rem 0;
    }}

    .progress-bar-fill {{
      height: 100%;
      border-radius: var(--radius-full);
      transition: width 0.3s;
    }}

    /* Glosarium Cards */
    .glossary-search-box {{
      display: flex;
      gap: 0.75rem;
      margin-bottom: 1.25rem;
      flex-wrap: wrap;
    }}

    .glossary-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 1rem;
    }}

    .glossary-card {{
      background: var(--white);
      border: 1px solid var(--slate-200);
      border-radius: var(--radius-md);
      padding: 1.15rem;
      box-shadow: var(--shadow-sm);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}

    .glossary-term {{
      font-size: 1.15rem;
      font-weight: 800;
      color: var(--primary-900);
      margin-bottom: 0.25rem;
    }}

    .glossary-def {{
      font-size: 0.88rem;
      color: var(--slate-700);
      line-height: 1.5;
      margin-bottom: 0.75rem;
    }}

    .glossary-src {{
      font-size: 0.78rem;
      color: var(--primary-700);
      background: var(--primary-50);
      padding: 0.4rem 0.65rem;
      border-radius: var(--radius-sm);
      border-left: 3px solid var(--primary-600);
    }}

    /* History & SVG Chart */
    .chart-container {{
      width: 100%;
      height: 240px;
      margin: 1.25rem 0;
      position: relative;
    }}

    .comparison-notice {{
      padding: 0.75rem 1rem;
      border-radius: var(--radius-md);
      font-size: 0.85rem;
      margin-bottom: 1.25rem;
      display: flex;
      align-items: center;
      gap: 0.65rem;
    }}

    .comparison-notice.valid {{
      background: var(--emerald-50);
      border: 1px solid var(--emerald-400);
      color: var(--emerald-800);
    }}

    .comparison-notice.disparate {{
      background: var(--accent-gold-50);
      border: 1px solid var(--accent-gold-400);
      color: var(--accent-gold-800);
    }}

    /* Review items in results */
    .review-item-card {{
      background: var(--white);
      border: 1px solid var(--slate-200);
      border-radius: var(--radius-md);
      padding: 1.25rem;
      margin-bottom: 1rem;
      box-shadow: var(--shadow-sm);
    }}

    .review-item-card.is-correct {{ border-left: 4px solid var(--emerald-600); }}
    .review-item-card.is-wrong {{ border-left: 4px solid var(--rose-600); }}
    .review-item-card.is-empty {{ border-left: 4px solid var(--slate-400); }}

    .explanation-box {{
      background: var(--slate-50);
      border-left: 3px solid var(--primary-600);
      padding: 0.85rem 1rem;
      border-radius: var(--radius-sm);
      margin-top: 0.75rem;
      font-size: 0.88rem;
    }}

    .explanation-source {{
      margin-top: 0.5rem;
      font-size: 0.8rem;
      color: var(--primary-700);
      font-weight: 600;
    }}

    /* Modals */
    .modal-backdrop {{
      position: fixed;
      top: 0; left: 0; right: 0; bottom: 0;
      background: rgba(15, 23, 42, 0.65);
      backdrop-filter: blur(3px);
      display: none;
      align-items: center;
      justify-content: center;
      z-index: 2000;
      padding: 1rem;
    }}

    .modal-backdrop.open {{
      display: flex;
    }}

    .modal-dialog {{
      background: var(--white);
      border-radius: var(--radius-lg);
      max-width: 580px;
      width: 100%;
      max-height: 90vh;
      overflow-y: auto;
      padding: 1.75rem;
      box-shadow: var(--shadow-xl);
      animation: modalFadeIn 0.2s ease-out;
    }}

    @keyframes modalFadeIn {{
      from {{ transform: scale(0.95); opacity: 0; }}
      to {{ transform: scale(1); opacity: 1; }}
    }}

    .modal-actions {{
      display: flex;
      justify-content: flex-end;
      gap: 0.75rem;
      margin-top: 1.5rem;
    }}

    /* Print styles */
    @media print {{
      .no-print, .civic-header, .palette-card, .cbt-action-bar, .modal-backdrop {{
        display: none !important;
      }}
      body {{
        background: #fff;
        color: #000;
      }}
      .app-main {{
        max-width: 100%;
        padding: 0;
      }}
      .review-item-card {{
        page-break-inside: avoid;
        border: 1px solid #ccc;
      }}
    }}
  </style>
</head>
<body>

  <!-- Official Civic Header -->
  <header class="civic-header no-print">
    <div class="header-container">
      <div class="brand-block" onclick="CBTApp.navigate('home')">
        <div class="brand-emblem">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/>
          </svg>
        </div>
        <div class="brand-title">
          <h1>SIMULASI CBT PERANGKAT DESA</h1>
          <p id="topRegionLabel">Fokus Kabupaten Tuban & Standar Nasional</p>
        </div>
      </div>

      <div class="header-nav">
        <button class="btn btn-outline btn-sm" onclick="CBTApp.navigate('home')" title="Halaman Utama">
          Beranda
        </button>
        <button class="btn btn-outline btn-sm" onclick="CBTApp.navigate('glossary')" title="Glosarium 36 Istilah Desa">
          Glosarium Desa
        </button>
        <button class="btn btn-outline btn-sm" onclick="CBTApp.navigate('history')" title="Riwayat & Grafik Nilai">
          Riwayat Skor
        </button>
        <button class="btn btn-outline btn-sm" onclick="CBTApp.openBackupModal()" title="Cadangan Data (Ekspor / Impor JSON)">
          Cadangan Data
        </button>

        <!-- A11y Font Resizer -->
        <div class="font-scale-control" title="Ukuran Font Aksesibilitas">
          <button class="font-scale-btn" id="fScaleSm" onclick="CBTApp.setFontScale('90%')">A-</button>
          <button class="font-scale-btn active" id="fScaleMd" onclick="CBTApp.setFontScale('100%')">A</button>
          <button class="font-scale-btn" id="fScaleLg" onclick="CBTApp.setFontScale('115%')">A+</button>
        </div>
      </div>
    </div>
  </header>

  <main class="app-main">

    <!-- Active Resume Session Alert -->
    <div id="resumeBanner" class="resume-card no-print" style="display:none;">
      <div>
        <strong style="color:var(--slate-900);">Sesi Ujian Aktif Ditemukan!</strong>
        <p style="font-size:0.85rem; color:var(--slate-700); margin-top:2px;">Anda memiliki sesi simulasi ujian yang belum selesai dengan progres tersimpan.</p>
      </div>
      <div style="display:flex; gap:0.5rem;">
        <button class="btn btn-emerald btn-sm" onclick="CBTApp.resumeSession()">Lanjutkan Ujian</button>
        <button class="btn btn-outline btn-sm" onclick="CBTApp.clearSession()">Hapus & Mulai Baru</button>
      </div>
    </div>

    <!-- Official Notice Banner -->
    <div class="disclaimer-banner no-print">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="color:var(--primary-600); flex-shrink:0;">
        <circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line>
      </svg>
      <div>
        <strong>PEMBERITAHUAN RESMI & PRIVASI PENUH:</strong>
        Aplikasi ini 100% berjalan lokal di browser Anda. Tidak ada data nama, jawaban, atau riwayat yang dikirim ke jaringan. Seluruh materi mengacu pada regulasi resmi terverifikasi (UU No. 6/2014 jo. UU No. 3/2024, PP No. 11/2019, Permendagri No. 84/2015, Permendagri No. 67/2017, Permendagri No. 20/2018, Perda Kab. Tuban No. 2/2016 jo. No. 16/2021). <em>Simulasi latihan mandiri, bukan ujian kedinasan resmi.</em>
      </div>
    </div>

    <!-- ======================================================================
         VIEW 1: BERANDA (HOME VIEW)
         ====================================================================== -->
    <section id="viewHome">
      <div class="hero-panel">
        <div class="hero-badge-row">
          <span class="badge-pill badge-cat">Bank Soal Database: 500 Butir</span>
          <span class="badge-pill badge-diff-mudah">Acak 100 Soal Otomatis</span>
          <span class="badge-pill badge-diff-sedang">Pilihan Jawaban Diacak Otomatis</span>
          <span class="badge-pill badge-diff-sulit">Durasi 100 Menit (60 Detik/Soal)</span>
          <span class="badge-pill badge-verified">100% Offline & Privat</span>
        </div>
        <h2>Persiapan Ujian Seleksi Perangkat Desa</h2>
        <p class="lead">Uji pemahaman dan kesiapan Anda dengan sistem Computer Assisted Test (CAT/CBT) mandiri. Dilengkapi database 500 bank soal terverifikasi, generator 100 soal acak per sesi, pilihan jawaban teracak otomatis tanpa kecurangan, glosarium istilah desa, analisis kelemahan materi, dan pelacak riwayat nilai.</p>

        <!-- Candidate Registration Box -->
        <div class="form-candidate-grid">
          <div class="form-group">
            <label for="inputCandidateName">Nama Lengkap Peserta (Opsional):</label>
            <input type="text" id="inputCandidateName" class="form-control" placeholder="Contoh: Ahmad Fauzi">
          </div>
          <div class="form-group">
            <label for="inputCandidateVillage">Desa / Kelurahan (Opsional):</label>
            <input type="text" id="inputCandidateVillage" class="form-control" placeholder="Contoh: Desa Sugihwaras">
          </div>
          <div class="form-group">
            <label for="selectRegion">Pilihan Wilayah Latihan:</label>
            <select id="selectRegion" class="form-control" onchange="CBTApp.handleRegionChange()">
              <option value="tuban">Kabupaten Tuban, Jawa Timur</option>
              <option value="nasional">Standar Nasional Indonesia</option>
            </select>
          </div>
        </div>

        <!-- Automatic Randomization & Anti-Cheating Banner (Replaces Manual Toggles) -->
        <div style="background:rgba(16, 185, 129, 0.15); padding:0.85rem 1.25rem; border-radius:var(--radius-md); border:1px solid rgba(16, 185, 129, 0.35); display:flex; gap:0.75rem; align-items:center;">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="color:var(--emerald-400); flex-shrink:0;">
            <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
          </svg>
          <div style="font-size:0.88rem; color:var(--white); line-height:1.4;">
            <strong>Sistem Integritas & Anti-Kecurangan Aktif:</strong> Seluruh 100 butir soal diundi secara acak proporsional dari bank database 500 soal (rasio sampling 20%), dan setiap susunan pilihan jawaban (A, B, C, D) diacak otomatis oleh sistem dengan sinkronisasi kunci jawaban presisi.
          </div>
        </div>
      </div>

      <!-- Action Cards Grid -->
      <div class="actions-grid">
        <div class="action-card">
          <div>
            <div class="action-card-header">
              <div class="action-card-icon" style="background:var(--primary-100); color:var(--primary-700);">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
              </div>
              <h3>Simulasi CAT Resmi</h3>
            </div>
            <p>100 butir soal acak dari database 500 soal sesuai kuota 12 kategori resmi. Waktu 100 menit, batas 60 detik/soal, penanda ragu-ragu, dan siklus otomatis soal belum terjawab.</p>
          </div>
          <button class="btn btn-gold btn-lg" onclick="CBTApp.confirmStartExam()">
            Mulai Simulasi CAT
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"></polyline></svg>
          </button>
        </div>

        <div class="action-card">
          <div>
            <div class="action-card-header">
              <div class="action-card-icon" style="background:var(--emerald-100); color:var(--emerald-700);">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg>
              </div>
              <h3>Latihan Mandiri</h3>
            </div>
            <p>Latihan belajar dengan pembahasan langsung setelah menjawab. Pilih per kategori atau 100 soal lengkap, atur jumlah soal dan timer sesuai kenyamanan belajar Anda.</p>
          </div>
          <button class="btn btn-primary" onclick="CBTApp.navigate('practice-config')">
            Atur Mode Latihan
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
          </button>
        </div>

        <div class="action-card">
          <div>
            <div class="action-card-header">
              <div class="action-card-icon" style="background:var(--accent-gold-100); color:var(--accent-gold-700);">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
              </div>
              <h3>Latihan Adaptif</h3>
            </div>
            <p>Sesi khusus drill pemulihan untuk mengulang soal yang dijawab salah pada sesi sebelumnya, soal yang belum sempat terjawab (kosong), atau soal yang masih ditandai ragu-ragu.</p>
          </div>
          <button class="btn btn-outline" onclick="CBTApp.openAdaptiveModal()">
            Buka Latihan Adaptif
          </button>
        </div>

        <div class="action-card">
          <div>
            <div class="action-card-header">
              <div class="action-card-icon" style="background:#e0f2fe; color:#0369a1;">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>
              </div>
              <h3>Glosarium 36 Istilah</h3>
            </div>
            <p>Kumpulan 36 istilah, singkatan penting, dan definisi hukum pemerintahan desa (Siltap, APB Desa, BPD, Silpa, Musrenbangdes, Siskeudes) yang dilengkapi pencarian instan.</p>
          </div>
          <button class="btn btn-outline" onclick="CBTApp.navigate('glossary')">
            Buka Glosarium
          </button>
        </div>
      </div>

      <!-- Category Distribution Table -->
      <div class="cbt-card">
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.5rem; margin-bottom:1rem;">
          <div>
            <h3 style="font-size:1.15rem; font-weight:800; color:var(--primary-900);">Struktur Bobot & Sebaran 12 Kategori Soal</h3>
            <p style="font-size:0.85rem; color:var(--slate-600);">Sistem mengundi 100 butir soal secara proporsional dari pool database 500 butir soal.</p>
          </div>
          <span class="badge-pill badge-cat">Total Database: 500 Butir</span>
        </div>

        <div class="table-container">
          <table class="cbt-table">
            <thead>
              <tr>
                <th style="width:40px; text-align:center;">No</th>
                <th>Kategori Materi</th>
                <th style="text-align:center;">Kuota Ujian</th>
                <th style="text-align:center;">Tersedia di Database</th>
                <th style="text-align:center;">Proporsi</th>
                <th>Fokus Materi & Rujukan Regulasi</th>
              </tr>
            </thead>
            <tbody id="distributionTableBody">
              <!-- Rendered via JS -->
            </tbody>
          </table>
        </div>
      </div>
    </section>

    <!-- ======================================================================
         VIEW 2: KONFIGURASI LATIHAN MANDIRI (PRACTICE CONFIG VIEW)
         ====================================================================== -->
    <section id="viewPracticeConfig" style="display:none;">
      <div class="cbt-card" style="max-width:700px; margin:0 auto;">
        <h2 style="font-size:1.35rem; font-weight:800; color:var(--primary-900); margin-bottom:0.5rem;">Pengaturan Mode Latihan Belajar</h2>
        <p style="font-size:0.88rem; color:var(--slate-600); margin-bottom:1.5rem;">Pada mode latihan, kunci jawaban dan pembahasan mendalam akan langsung ditampilkan setelah Anda memilih jawaban.</p>

        <div class="form-group" style="margin-bottom:1.25rem;">
          <label for="practiceCategorySelect" style="color:var(--slate-800);">Pilih Kategori Materi:</label>
          <select id="practiceCategorySelect" class="form-control">
            <option value="all">Semua Kategori (Database 500 Soal)</option>
            <!-- Populated via JS -->
          </select>
        </div>

        <div class="form-group" style="margin-bottom:1.25rem;">
          <label for="practiceCountSelect" style="color:var(--slate-800);">Jumlah Soal Latihan:</label>
          <select id="practiceCountSelect" class="form-control">
            <option value="10">10 Soal (Latihan Cepat)</option>
            <option value="25" selected>25 Soal (Standar)</option>
            <option value="50">50 Soal (Mendalam)</option>
            <option value="100">100 Soal (Simulasi Lengkap)</option>
          </select>
        </div>

        <div class="form-group" style="margin-bottom:1.25rem;">
          <label for="practiceShuffleSelect" style="color:var(--slate-800);">Pengacakan Soal & Pilihan:</label>
          <select id="practiceShuffleSelect" class="form-control">
            <option value="yes" selected>Acak Soal dan Acak Opsi Jawaban</option>
            <option value="no">Urut Sesuai Database Asli</option>
          </select>
        </div>

        <div class="form-group" style="margin-bottom:1.75rem;">
          <label style="color:var(--slate-800);">Gunakan Timer Simulasi?</label>
          <div style="display:flex; align-items:center; gap:0.75rem; margin-top:0.35rem;">
            <input type="checkbox" id="practiceTimerToggle" style="width:18px; height:18px;">
            <span style="font-size:0.88rem; color:var(--slate-700);">Aktifkan batas waktu 60 detik per soal</span>
          </div>
        </div>

        <div style="display:flex; justify-content:space-between; gap:1rem;">
          <button class="btn btn-outline" onclick="CBTApp.navigate('home')">Kembali ke Beranda</button>
          <button class="btn btn-primary" onclick="CBTApp.startPracticeSession()">Mulai Latihan</button>
        </div>
      </div>
    </section>

    <!-- ======================================================================
         VIEW 3: UJIAN SIMULASI CAT REALISTIS (EXAM VIEW)
         ====================================================================== -->
    <section id="viewExam" style="display:none;">
      <!-- Top Status Bar -->
      <div class="exam-top-bar">
        <div class="candidate-info-chip">
          <div class="candidate-avatar" id="avatarInitial">P</div>
          <div class="candidate-text">
            <h4 id="barCandidateName">Nama Peserta</h4>
            <p><span id="barRegionBadge">Kabupaten Tuban</span> • <span id="barModeBadge">Simulasi CAT (100 Menit)</span></p>
          </div>
        </div>

        <div class="timers-wrapper">
          <div class="timer-badge total-timer" id="boxTotalTimer">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
            <span id="displayTotalTimer">100:00</span>
          </div>
          <div class="timer-badge question-timer" id="boxQuestionTimer">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v4M12 18v4M4.93 4.93l2.83 2.83M16.24 16.24l2.83 2.83M2 12h4M18 12h4M4.93 19.07l2.83-2.83M16.24 7.76l2.83-2.83"/></svg>
            <span id="displayQuestionTimer">60s</span>
          </div>
        </div>
      </div>

      <!-- Main CAT Layout -->
      <div class="cbt-exam-layout">
        <div class="question-card">
          <div>
            <div class="question-meta-row">
              <div class="question-number-badge" id="qDisplayIndex">
                Soal Nomor 1 dari 100
              </div>
              <div class="badges-group">
                <span class="badge-pill badge-cat" id="qCategoryPill">Kategori</span>
                <span class="badge-pill badge-diff-sedang" id="qDifficultyPill">SEDANG</span>
                <span class="badge-pill" id="qRoundPill" style="display:none; background:var(--rose-100); color:var(--rose-700);">Putaran Prioritas Kosong</span>
              </div>
            </div>

            <!-- Question Body -->
            <div class="question-text" id="qQuestionText">
              Memuat butir pertanyaan...
            </div>

            <!-- Options List (A, B, C, D) -->
            <div class="options-list" id="qOptionsList">
              <!-- Rendered via JS -->
            </div>

            <!-- Instant Feedback (Practice Mode Only) -->
            <div id="practiceFeedbackBox" class="explanation-box" style="display:none;">
              <div class="explanation-title" id="practiceFeedbackTitle" style="font-weight:700; color:var(--emerald-700); margin-bottom:0.35rem;">
                Pembahasan & Kunci Jawaban
              </div>
              <div class="explanation-content" id="practiceFeedbackContent"></div>
              <div class="explanation-source" id="practiceFeedbackSource"></div>
            </div>
          </div>

          <!-- CBT Navigation Action Bar -->
          <div class="cbt-action-bar">
            <div class="cbt-action-left">
              <button class="btn btn-outline" id="btnPrevQuestion" onclick="CBTApp.prevQuestion()">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="15 18 9 12 15 6"></polyline></svg>
                Sebelumnya
              </button>
              <button class="btn btn-outline" id="btnNextQuestion" onclick="CBTApp.skipOrNextQuestion()">
                Lewati / Berikutnya
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"></polyline></svg>
              </button>
              <button class="btn btn-outline btn-sm" id="btnFlagQuestion" onclick="CBTApp.toggleFlagCurrentQuestion()" title="Tandai ragu-ragu (Shortcut: R)">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 15s1-1 4-1 5 2 8 2 4-1 4-1V3s-1 1-4 1-5-2-8-2-4 1-4 1z"></path><line x1="4" y1="22" x2="4" y2="15"></line></svg>
                <span id="btnFlagLabel">Ragu-ragu (R)</span>
              </button>
            </div>

            <div class="cbt-action-right">
              <button class="btn btn-danger" onclick="CBTApp.confirmFinishExam()">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
                Selesaikan Ujian
              </button>
            </div>
          </div>
        </div>

        <!-- 100-Question Palette Sidebar -->
        <aside class="palette-card" id="paletteDrawer">
          <div class="palette-header">
            <h3>Nomor Soal</h3>
            <div id="paletteAnswerCount" style="font-size:0.8rem; font-weight:700; color:var(--primary-700);">0 / 100</div>
          </div>

          <div class="palette-filter-bar">
            <button class="palette-filter-btn active" id="pFilterAll" onclick="CBTApp.setPaletteFilter('all')">Semua</button>
            <button class="palette-filter-btn" id="pFilterDone" onclick="CBTApp.setPaletteFilter('done')">Dijawab</button>
            <button class="palette-filter-btn" id="pFilterFlag" onclick="CBTApp.setPaletteFilter('flag')">Ragu</button>
            <button class="palette-filter-btn" id="pFilterEmpty" onclick="CBTApp.setPaletteFilter('empty')">Belum</button>
          </div>

          <div class="palette-legend">
            <div class="legend-item"><span class="legend-dot" style="background:var(--emerald-600);"></span> Terjawab</div>
            <div class="legend-item"><span class="legend-dot" style="background:var(--accent-gold-500);"></span> Ragu-ragu</div>
            <div class="legend-item"><span class="legend-dot" style="background:var(--white); border:2px solid var(--primary-600);"></span> Aktif</div>
            <div class="legend-item"><span class="legend-dot" style="background:var(--white); border:1px solid var(--slate-300);"></span> Belum</div>
          </div>

          <div class="grid-palette" id="gridQuestionButtons">
            <!-- Buttons rendered via JS -->
          </div>
        </aside>
      </div>
    </section>

    <!-- ======================================================================
         VIEW 4: HASIL, ANALISIS KELEMAHAN & EVALUASI (RESULTS VIEW)
         ====================================================================== -->
    <section id="viewResults" style="display:none;">
      <!-- Results Hero Card -->
      <div class="results-hero">
        <div class="results-hero-grid">
          <div>
            <div class="hero-badge-row" style="justify-content:flex-start;">
              <span class="badge-pill badge-cat" id="resBadgeMode">Mode Simulasi CAT</span>
              <span class="badge-pill badge-diff-mudah" id="resBadgeRegion">Kabupaten Tuban</span>
              <span class="badge-pill" style="background:rgba(255,255,255,0.2); color:#fff;" id="resDateBadge">18 Oktober 2026</span>
            </div>
            <h2 style="font-size:1.8rem; font-weight:800; margin-bottom:0.25rem;" id="resCandidateHeading">Hasil Simulasi Ujian: Peserta</h2>
            <p style="font-size:0.92rem; opacity:0.9;" id="resCandidateSubheading">Desa Sugihwaras • Pelaksanaan Selesai</p>

            <div class="results-stats-row">
              <div class="stat-box">
                <div style="font-size:0.75rem; color:var(--slate-300);">Total Soal</div>
                <div class="stat-box-num" id="resTotalSoal">100</div>
              </div>
              <div class="stat-box">
                <div style="font-size:0.75rem; color:var(--slate-300);">Benar</div>
                <div class="stat-box-num benar" id="resCountBenar">0</div>
              </div>
              <div class="stat-box">
                <div style="font-size:0.75rem; color:var(--slate-300);">Salah</div>
                <div class="stat-box-num salah" id="resCountSalah">0</div>
              </div>
              <div class="stat-box">
                <div style="font-size:0.75rem; color:var(--slate-300);">Kosong</div>
                <div class="stat-box-num kosong" id="resCountKosong">0</div>
              </div>
              <div class="stat-box">
                <div style="font-size:0.75rem; color:var(--slate-300);">Waktu Digunakan</div>
                <div class="stat-box-num" id="resTimeUsed" style="font-size:1.05rem; padding-top:4px;">00:00</div>
              </div>
            </div>
          </div>

          <div class="results-score-badge">
            <div style="font-size:0.75rem; font-weight:700; letter-spacing:0.5px; color:var(--slate-300);">SKOR AKHIR SIMULASI</div>
            <div class="score-value" id="resScoreValue">0</div>
            <div style="font-size:0.82rem; color:var(--slate-200);">Skala 0 – 100 • Akurasi: <span id="resAccuracyPercent">0%</span></div>
          </div>
        </div>
      </div>

      <!-- Action Toolbar -->
      <div style="display:flex; justify-content:space-between; align-items:center; gap:0.75rem; margin-bottom:1.5rem; flex-wrap:wrap;" class="no-print">
        <div style="display:flex; gap:0.5rem; flex-wrap:wrap;">
          <button class="btn btn-emerald btn-sm" onclick="CBTApp.startAdaptiveFromResults('wrong')">
            Ulangi Jawaban Salah
          </button>
          <button class="btn btn-outline btn-sm" onclick="CBTApp.startAdaptiveFromResults('empty')">
            Ulangi Soal Kosong
          </button>
          <button class="btn btn-outline btn-sm" onclick="CBTApp.navigate('glossary')">
            Buka Glosarium Terkait
          </button>
        </div>
        <div style="display:flex; gap:0.5rem; flex-wrap:wrap;">
          <button class="btn btn-outline btn-sm" onclick="CBTApp.exportCSV()">Ekspor CSV</button>
          <button class="btn btn-outline btn-sm" onclick="CBTApp.exportJSON()">Ekspor JSON</button>
          <button class="btn btn-primary btn-sm" onclick="window.print()">Cetak Laporan</button>
        </div>
      </div>

      <!-- Section: Analisis Kelemahan & Rekomendasi Belajar (Feature 2) -->
      <div class="cbt-card">
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.5rem; margin-bottom:1rem;">
          <div>
            <h3 style="font-size:1.2rem; font-weight:800; color:var(--primary-900);">Analisis Kelemahan & Rekomendasi Pembelajaran</h3>
            <p style="font-size:0.85rem; color:var(--slate-600);">Diurutkan dari kategori materi yang membutuhkan penguatan paling mendalam.</p>
          </div>
          <span class="badge-pill badge-cat">Berdasarkan Hasil Sesi Terakhir</span>
        </div>

        <div id="weaknessListContainer">
          <!-- Injected via JS -->
        </div>
      </div>

      <!-- Section: Rekapitulasi 12 Kategori -->
      <div class="cbt-card">
        <h3 style="font-size:1.15rem; font-weight:800; color:var(--primary-900); margin-bottom:0.75rem;">Rekapitulasi Nilai Per Kategori Materi</h3>
        <div class="table-container">
          <table class="cbt-table">
            <thead>
              <tr>
                <th style="width:40px; text-align:center;">No</th>
                <th>Kategori Materi</th>
                <th style="text-align:center;">Total</th>
                <th style="text-align:center;">Benar</th>
                <th style="text-align:center;">Salah</th>
                <th style="text-align:center;">Kosong</th>
                <th style="text-align:center;">Akurasi</th>
                <th>Status Penguasaan</th>
              </tr>
            </thead>
            <tbody id="resultsCategoryTableBody">
              <!-- Rendered via JS -->
            </tbody>
          </table>
        </div>
      </div>

      <!-- Tabbed Review Items -->
      <div class="cbt-card">
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.75rem; margin-bottom:1.25rem;">
          <div style="display:flex; gap:0.35rem; flex-wrap:wrap;">
            <button class="btn btn-outline btn-sm active" id="tabRevWrong" onclick="CBTApp.setReviewTab('wrong')">Jawaban Salah</button>
            <button class="btn btn-outline btn-sm" id="tabRevEmpty" onclick="CBTApp.setReviewTab('empty')">Soal Kosong</button>
            <button class="btn btn-outline btn-sm" id="tabRevCorrect" onclick="CBTApp.setReviewTab('correct')">Jawaban Benar</button>
            <button class="btn btn-outline btn-sm" id="tabRevAll" onclick="CBTApp.setReviewTab('all')">Semua Soal (100)</button>
          </div>

          <div style="display:flex; gap:0.5rem; align-items:center;">
            <input type="text" id="reviewSearchInput" class="form-control" placeholder="Cari pembahasan / pasal..." oninput="CBTApp.renderActiveReviewTab()" style="max-width:240px; padding:0.4rem 0.65rem; font-size:0.85rem;">
          </div>
        </div>

        <div id="evalReviewContainer">
          <!-- Rendered via JS -->
        </div>
      </div>
    </section>

    <!-- ======================================================================
         VIEW 5: GLOSARIUM ISTILAH DESA (GLOSSARY VIEW)
         ====================================================================== -->
    <section id="viewGlossary" style="display:none;">
      <div class="cbt-card">
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.5rem; margin-bottom:1.25rem;">
          <div>
            <h2 style="font-size:1.35rem; font-weight:800; color:var(--primary-900);">Glosarium Istilah & Regulasi Pemerintahan Desa</h2>
            <p style="font-size:0.88rem; color:var(--slate-600);">Kumpulan 36 istilah, singkatan, dan landasan hukum resmi yang sering keluar dalam seleksi perangkat desa.</p>
          </div>
          <button class="btn btn-outline btn-sm" onclick="CBTApp.navigate('home')">Kembali ke Beranda</button>
        </div>

        <div class="glossary-search-box">
          <input type="text" id="glossarySearchInput" class="form-control" placeholder="Cari istilah, nama kepanjangan, atau kata kunci (misal: Siltap, APB Desa, BPD, Silpa)..." oninput="CBTApp.renderGlossary()" style="flex:1; min-width:240px;">
          <select id="glossaryCategorySelect" class="form-control" onchange="CBTApp.renderGlossary()" style="max-width:240px;">
            <option value="all">Semua Kategori</option>
            <option value="Keuangan & APB Desa">Keuangan & APB Desa</option>
            <option value="Perencanaan & Pembangunan">Perencanaan & Pembangunan</option>
            <option value="Kelembagaan & Musyawarah">Kelembagaan & Musyawarah</option>
            <option value="Pemerintahan & Organisasi">Pemerintahan & Organisasi</option>
            <option value="Regulasi & Tata Kelola">Regulasi & Tata Kelola</option>
            <option value="Perekonomian & BUMDes">Perekonomian & BUMDes</option>
          </select>
        </div>

        <div class="glossary-grid" id="glossaryListContainer">
          <!-- Populated via JS -->
        </div>
      </div>
    </section>

    <!-- ======================================================================
         VIEW 6: RIWAYAT NILAI & GRAFIK TREN (HISTORY VIEW)
         ====================================================================== -->
    <section id="viewHistory" style="display:none;">
      <div class="cbt-card">
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.5rem; margin-bottom:1rem;">
          <div>
            <h2 style="font-size:1.35rem; font-weight:800; color:var(--primary-900);">Riwayat & Perkembangan Nilai Simulasi</h2>
            <p style="font-size:0.88rem; color:var(--slate-600);">Pantau tren skor latihan dan komparasi hasil antar-sesi secara adil.</p>
          </div>
          <div style="display:flex; gap:0.5rem;">
            <button class="btn btn-outline btn-sm" onclick="CBTApp.confirmClearHistory()">Hapus Riwayat</button>
            <button class="btn btn-outline btn-sm" onclick="CBTApp.navigate('home')">Kembali ke Beranda</button>
          </div>
        </div>

        <!-- Disparity / Valid Comparison Banner -->
        <div id="historyComparisonBox">
          <!-- Injected via JS -->
        </div>

        <!-- SVG Line/Bar Chart -->
        <div style="background:var(--slate-50); border:1px solid var(--slate-200); border-radius:var(--radius-md); padding:1rem;">
          <h4 style="font-size:0.95rem; font-weight:800; color:var(--primary-900); margin-bottom:0.5rem;">Grafik Perkembangan Skor (0 - 100)</h4>
          <div class="chart-container" id="chartContainer">
            <!-- SVG rendered via JS -->
          </div>
        </div>

        <!-- History Table -->
        <div class="table-container" style="margin-top:1.5rem;">
          <table class="cbt-table">
            <thead>
              <tr>
                <th style="text-align:center;">No</th>
                <th>Tanggal & Waktu</th>
                <th>Peserta</th>
                <th>Jenis Sesi</th>
                <th style="text-align:center;">Soal</th>
                <th style="text-align:center;">Benar</th>
                <th style="text-align:center;">Skor</th>
                <th style="text-align:center;">Akurasi</th>
                <th>Kategori Terlemah</th>
              </tr>
            </thead>
            <tbody id="historyTableBody">
              <!-- Rendered via JS -->
            </tbody>
          </table>
        </div>
      </div>
    </section>

  </main>

  <!-- Official Footer -->
  <footer class="civic-footer no-print" style="background:var(--primary-900); color:var(--slate-300); padding:1.5rem 1.25rem; font-size:0.82rem; border-top:1px solid rgba(255,255,255,0.1);">
    <div style="max-width:1300px; margin:0 auto; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.75rem;">
      <p>© 2026 Simulasi CBT Ujian Perangkat Desa. Database 500 Soal dengan Pengacakan Otomatis & Anti-Kecurangan.</p>
      <p>100% Offline • Terverifikasi Berdasarkan UU No. 6/2014 jo. UU No. 3/2024 & Regulasi Kabupaten Tuban Jawa Timur.</p>
    </div>
  </footer>

  <!-- ======================================================================
       MODAL CONFIRMATION DIALOGS
       ====================================================================== -->
  
  <!-- Modal: Mulai Ujian Confirmation -->
  <div class="modal-backdrop" id="modalStartExam">
    <div class="modal-dialog">
      <h3 style="font-size:1.25rem; font-weight:800; color:var(--primary-900); margin-bottom:0.75rem;">Konfirmasi Mulai Simulasi CAT</h3>
      <p style="font-size:0.92rem; color:var(--slate-700); line-height:1.5; margin-bottom:1rem;">
        Sistem akan mengambil <strong>100 butir soal secara proporsional dari database 500 soal</strong>, mengacak urutan soal dan susunan pilihan jawaban (A, B, C, D) secara otomatis tanpa celah kecurangan.<br><br>
        Waktu ujian: <strong>100 menit (6.000 detik)</strong> dengan batas maksimal <strong>60 detik</strong> per kunjungan soal.<br><br>
        <span style="color:var(--rose-600); font-weight:700;">Perhatian: Timer akan langsung berjalan setelah tombol ditekan.</span>
      </p>
      <div class="modal-actions">
        <button class="btn btn-outline" onclick="CBTApp.closeModals()">Batal</button>
        <button class="btn btn-primary" onclick="CBTApp.startExamNow()">Mulai Sekarang</button>
      </div>
    </div>
  </div>

  <!-- Modal: CAT Pre-Finish Status Summary (Feature 1) -->
  <div class="modal-backdrop" id="modalFinishExam">
    <div class="modal-dialog">
      <h3 style="font-size:1.25rem; font-weight:800; color:var(--primary-900); margin-bottom:0.5rem;">Ringkasan Status Sebelum Pengakhiran Ujian</h3>
      <p style="font-size:0.88rem; color:var(--slate-600); margin-bottom:1rem;">Periksa kembali rekapitulasi status seluruh butir soal sebelum Anda menyelesaikan ujian.</p>

      <div class="status-summary-grid">
        <div class="status-pill-box answered">
          <div class="status-pill-num" id="preFinishAnswered">0</div>
          <div class="status-pill-label">Sudah Dijawab</div>
        </div>
        <div class="status-pill-box flagged">
          <div class="status-pill-num" id="preFinishFlagged">0</div>
          <div class="status-pill-label">Ragu-Ragu</div>
        </div>
        <div class="status-pill-box empty">
          <div class="status-pill-num" id="preFinishEmpty">0</div>
          <div class="status-pill-label">Belum Dijawab</div>
        </div>
      </div>

      <!-- Critical Warnings -->
      <div id="preFinishWarningBox" style="margin:1rem 0;"></div>

      <!-- Jump chips for unanswered or flagged -->
      <div id="preFinishJumpWrap" style="display:none; margin-bottom:1rem;">
        <label style="font-size:0.8rem; font-weight:700; color:var(--slate-700);">Klik nomor di bawah untuk langsung memeriksa soal:</label>
        <div class="clickable-nums-wrap" id="preFinishJumpChips"></div>
      </div>

      <div class="modal-actions">
        <button class="btn btn-outline" onclick="CBTApp.closeModals()">Kembali Tinjau Soal</button>
        <button class="btn btn-danger" onclick="CBTApp.finishExam('USER_SUBMIT')">Tetap Selesaikan Ujian</button>
      </div>
    </div>
  </div>

  <!-- Modal: Latihan Adaptif Chooser (Feature 3) -->
  <div class="modal-backdrop" id="modalAdaptiveChoice">
    <div class="modal-dialog">
      <h3 style="font-size:1.25rem; font-weight:800; color:var(--primary-900); margin-bottom:0.5rem;">Pilih Sesi Latihan Adaptif</h3>
      <p style="font-size:0.88rem; color:var(--slate-600); margin-bottom:1rem;">Latihan adaptif fokus pada butir soal yang paling membutuhkan perbaikan dari sesi sebelumnya.</p>

      <div style="display:flex; flex-direction:column; gap:0.75rem;">
        <button class="btn btn-outline" style="text-align:left; justify-content:flex-start; padding:0.85rem;" onclick="CBTApp.startAdaptiveDrill('wrong')">
          <div>
            <div style="font-weight:800; color:var(--rose-700);">1. Ulangi Soal Salah (Weakness Recovery)</div>
            <div style="font-size:0.8rem; color:var(--slate-600);">Mengulang soal-soal yang pernah Anda jawab salah untuk memastikan pemahaman.</div>
          </div>
        </button>

        <button class="btn btn-outline" style="text-align:left; justify-content:flex-start; padding:0.85rem;" onclick="CBTApp.startAdaptiveDrill('empty')">
          <div>
            <div style="font-weight:800; color:var(--primary-700);">2. Ulangi Soal Kosong / Terlewat</div>
            <div style="font-size:0.8rem; color:var(--slate-600);">Mengerjakan kembali soal-soal yang belum sempat dijawab karena keterbatasan waktu.</div>
          </div>
        </button>

        <button class="btn btn-outline" style="text-align:left; justify-content:flex-start; padding:0.85rem;" onclick="CBTApp.startAdaptiveDrill('flagged')">
          <div>
            <div style="font-weight:800; color:var(--accent-gold-700);">3. Ulangi Soal Ragu-ragu (Penanda)</div>
            <div style="font-size:0.8rem; color:var(--slate-600);">Memantapkan pemahaman pada soal-soal yang sebelumnya Anda tandai ragu-ragu.</div>
          </div>
        </button>
      </div>

      <div class="modal-actions">
        <button class="btn btn-outline" onclick="CBTApp.closeModals()">Tutup</button>
      </div>
    </div>
  </div>

  <!-- Modal: Cadangan Lokal (Ekspor & Impor JSON) (Feature 8) -->
  <div class="modal-backdrop" id="modalBackupRestore">
    <div class="modal-dialog">
      <h3 style="font-size:1.25rem; font-weight:800; color:var(--primary-900); margin-bottom:0.5rem;">Cadangan Data Lokal (Ekspor & Impor JSON)</h3>
      <p style="font-size:0.88rem; color:var(--slate-600); margin-bottom:1.25rem;">Cadangkan riwayat ujian dan pengaturan ke file JSON lokal, atau pulihkan data dari file cadangan sebelumnya. File divalidasi ketat dan diproses offline.</p>

      <div style="background:var(--slate-50); border:1px solid var(--slate-200); border-radius:var(--radius-md); padding:1rem; margin-bottom:1.25rem;">
        <h4 style="font-size:0.95rem; font-weight:800; color:var(--primary-900); margin-bottom:0.25rem;">Ekspor Cadangan</h4>
        <p style="font-size:0.82rem; color:var(--slate-600); margin-bottom:0.75rem;">Unduh data riwayat latihan, skor, dan preferensi akun Anda dalam format JSON.</p>
        <button class="btn btn-primary btn-sm" onclick="CBTApp.exportBackupJSON()">
          Unduh File Cadangan JSON
        </button>
      </div>

      <div style="background:var(--slate-50); border:1px solid var(--slate-200); border-radius:var(--radius-md); padding:1rem;">
        <h4 style="font-size:0.95rem; font-weight:800; color:var(--primary-900); margin-bottom:0.25rem;">Impor & Pulihkan Data</h4>
        <p style="font-size:0.82rem; color:var(--slate-600); margin-bottom:0.75rem;">Pilih file cadangan JSON yang valid (maksimal ukuran 2 MB).</p>
        <input type="file" id="backupFileInput" accept=".json" class="form-control" style="font-size:0.85rem; margin-bottom:0.75rem;">
        <div style="display:flex; gap:0.5rem;">
          <button class="btn btn-emerald btn-sm" onclick="CBTApp.importBackupJSON('merge')">Gabungkan Riwayat</button>
          <button class="btn btn-outline btn-sm" onclick="CBTApp.importBackupJSON('replace')">Ganti Penuh</button>
        </div>
      </div>

      <div class="modal-actions">
        <button class="btn btn-outline" onclick="CBTApp.closeModals()">Tutup</button>
      </div>
    </div>
  </div>

  <!-- Modal: Waktu Habis Alert -->
  <div class="modal-backdrop" id="modalTimeExpired">
    <div class="modal-dialog">
      <h3 style="font-size:1.25rem; font-weight:800; color:var(--rose-700); margin-bottom:0.5rem;">Waktu Ujian 100 Menit Telah Habis!</h3>
      <p style="font-size:0.92rem; color:var(--slate-700); line-height:1.5;">
        Batas waktu ujian telah berakhir. Seluruh jawaban Anda yang telah tersimpan telah direkapitulasi secara otomatis untuk perhitungan nilai akhir.
      </p>
      <div class="modal-actions">
        <button class="btn btn-primary" onclick="CBTApp.closeModals(); CBTApp.showResultsView();">Lihat Laporan Hasil</button>
      </div>
    </div>
  </div>

  <!-- ======================================================================
       JAVASCRIPT APPLICATION ENGINE
       ====================================================================== -->
  <script>
    // Master Database of 500 Questions
    const MASTER_QUESTIONS = {questions_json};

    // Master Database of 36 Village Terms (Glossary)
    const GLOSSARY_DATA = {glossary_json};

    // Category Distribution Schema (Exam quota & Database count)
    const CATEGORIES_SPEC = [
      {{ name: "Pemerintahan desa, struktur organisasi, tugas dan fungsi perangkat desa", count: 20, inDb: 100, focus: "UU No. 6/2014 jo. UU No. 3/2024, Permendagri 84/2015, Permendagri 67/2017, PP 11/2019, Siltap, usia & pensiun" }},
      {{ name: "Peraturan perundang-undangan dan tata kelola pemerintahan", count: 12, inDb: 60, focus: "Hierarki UU 12/2011, produk hukum desa Permendagri 111/2014, asas desa, Perda Tuban 2/2016 jo 16/2021, Perbup Tuban 11/2022" }},
      {{ name: "Pancasila, UUD 1945, dan wawasan kebangsaan", count: 10, inDb: 50, focus: "Pengamalan Sila 1-5 di desa, Pembukaan UUD 1945 alinea IV, Pasal 1(2), 27(3), Bhinneka Tunggal Ika, Wawasan Nusantara" }},
      {{ name: "Administrasi pemerintahan, surat-menyurat, dan pengarsipan", count: 10, inDb: 50, focus: "Permendagri 47/2016 (5 buku adm desa), tata naskah dinas, buku ekspedisi, kop surat, SK Kades, arsip dinamis" }},
      {{ name: "Keuangan desa, APB Desa, dan aset desa", count: 10, inDb: 50, focus: "Permendagri 20/2018 (PKPKD, PPKD, Siskeudes), Permendagri 1/2016 (Aset desa, sewa max 3 th), 5 bidang belanja desa" }},
      {{ name: "Pembangunan desa, perencanaan, dan pemberdayaan masyarakat", count: 8, inDb: 40, focus: "Permendesa 21/2020 (RPJM Desa, RKP Desa akhir Sept, Musrenbangdes), SDGs Desa, BUMDes PP 11/2021, LKD Permendagri 18/2018" }},
      {{ name: "BPD, kelembagaan desa, dan musyawarah", count: 5, inDb: 25, focus: "UU 6/2014 Pasal 55, Permendagri 110/2016 (3 fungsi BPD, larangan rangkap jabatan), Musdes, LKPPD 3 bulan" }},
      {{ name: "Bahasa Indonesia", count: 7, inDb: 35, focus: "EYD V kata baku (antre, izin, kuitansi, jadwal), kapitalisasi naskah dinas, kalimat efektif bebas pleonasme, tanda baca" }},
      {{ name: "Matematika dan numerik", count: 6, inDb: 30, focus: "Persentase APB Desa, konversi hektar lahan bengkok, potongan pajak PPh 22, rata-rata pupuk, deret bilangan, perbandingan berbalik nilai" }},
      {{ name: "Logika dan penalaran", count: 5, inDb: 25, focus: "Silogisme kategorial seragam dinas, penalaran jadwal piket staf, modus tollens genangan air, himpunan bantuan bansos, mediasi sengketa batas" }},
      {{ name: "Pengetahuan umum", count: 4, inDb: 20, focus: "Hari Jadi Tuban 12 Nov 1293 (Ronggolawe), Makam Sunan Bonang, hierarki pemda, filosofi bulu Garuda Pancasila" }},
      {{ name: "Komputer dasar dan pelayanan publik", count: 3, inDb: 15, focus: "Microsoft Excel (=SUM, =AVERAGE), Word Mail Merge surat massal desa, UU PDP No. 27/2022 perlindungan NIK warga" }}
    ];

    // Safe Randomization Helpers (Fisher-Yates)
    function shuffleArray(array) {{
      for (let i = array.length - 1; i > 0; i--) {{
        const j = Math.floor(Math.random() * (i + 1));
        const temp = array[i];
        array[i] = array[j];
        array[j] = temp;
      }}
      return array;
    }}

    function generateExam100Questions(masterList, categorySpec, randomizeQuestions = true, randomizeOptions = true) {{
      let sampled = [];
      categorySpec.forEach(cat => {{
        const pool = masterList.filter(q => q.category === cat.name);
        const shuffledPool = randomizeQuestions ? shuffleArray([...pool]) : [...pool];
        const picked = shuffledPool.slice(0, cat.count);
        sampled.push(...picked);
      }});

      if (randomizeQuestions) {{
        shuffleArray(sampled);
      }}

      return sampled.map((q, idx) => {{
        const originalCorrectText = q.options[q.answer];
        const optionsList = [...q.options];
        if (randomizeOptions) {{
          shuffleArray(optionsList);
        }}
        const newAnswerIndex = optionsList.indexOf(originalCorrectText);

        return {{
          ...q,
          number: idx + 1,
          options: optionsList,
          answer: newAnswerIndex,
          originalAnswer: q.answer,
          originalId: q.id
        }};
      }});
    }}

    // Safe Storage Wrappers (Resilience against Quota / Incognito)
    function safeGetStorage(key, defaultVal) {{
      try {{
        const item = localStorage.getItem(key);
        return item ? JSON.parse(item) : defaultVal;
      }} catch (e) {{
        console.warn('Storage read fallback:', e);
        return defaultVal;
      }}
    }}

    function safeSetStorage(key, value) {{
      try {{
        localStorage.setItem(key, JSON.stringify(value));
        return true;
      }} catch (e) {{
        console.warn('Storage write fallback (in-memory mode active):', e);
        return false;
      }}
    }}

    // ==========================================================================
    // MAIN CBT CONTROLLER
    // ==========================================================================
    const CBTApp = {{
      mode: 'exam', // 'exam' | 'practice' | 'adaptive'
      region: 'tuban',
      candidateName: '',
      candidateVillage: '',
      
      questions: [],
      currentIndex: 0,
      userAnswers: {{}},
      flaggedQuestions: {{}},
      visitedCount: {{}},
      
      examDurationMs: 100 * 60 * 1000,
      questionDurationMs: 60 * 1000,
      examStartTime: null,
      questionVisitStartTime: null,
      timerInterval: null,
      isExamRunning: false,
      examSubmitted: false,
      inPriorityCycle: false,
      
      paletteFilter: 'all', // 'all' | 'done' | 'flag' | 'empty'
      activeReviewTab: 'wrong', // 'wrong' | 'empty' | 'correct' | 'all'
      
      STORAGE_KEY: 'perangkat_desa_cbt_session_v3',
      HISTORY_KEY: 'cbt_exam_history_v2',

      init() {{
        this.renderDistributionTable();
        this.populateCategoryDropdowns();
        this.renderGlossary();
        this.checkExistingSession();
        this.setupKeyboardShortcuts();
      }},

      renderDistributionTable() {{
        const tbody = document.getElementById('distributionTableBody');
        if (!tbody) return;
        let html = '';
        CATEGORIES_SPEC.forEach((item, idx) => {{
          const prop = (item.count / 100 * 100).toFixed(0);
          html += `
            <tr>
              <td style="text-align:center; font-weight:700; color:var(--slate-500);">${{idx + 1}}</td>
              <td style="font-weight:600; color:var(--primary-900);">${{item.name}}</td>
              <td style="text-align:center; font-weight:700; color:var(--primary-700);">${{item.count}} Soal</td>
              <td style="text-align:center; font-weight:700; color:var(--emerald-600);">${{item.inDb}} Soal</td>
              <td style="text-align:center;"><span class="badge-pill badge-cat">${{prop}}%</span></td>
              <td style="font-size:0.8rem; color:var(--slate-600);">${{item.focus}}</td>
            </tr>
          `;
        }});
        tbody.innerHTML = html;
      }},

      populateCategoryDropdowns() {{
        const pSelect = document.getElementById('practiceCategorySelect');
        if (!pSelect) return;
        let pOptions = '<option value="all">Semua Kategori (Database 500 Soal)</option>';
        CATEGORIES_SPEC.forEach(cat => {{
          pOptions += `<option value="${{cat.name}}">${{cat.name}} (${{cat.inDb}} di Database)</option>`;
        }});
        pSelect.innerHTML = pOptions;
      }},

      handleRegionChange() {{
        const sel = document.getElementById('selectRegion');
        this.region = sel ? sel.value : 'tuban';
        const topLabel = document.getElementById('topRegionLabel');
        if (topLabel) {{
          topLabel.textContent = this.region === 'tuban' 
            ? 'Fokus Kabupaten Tuban & Standar Nasional'
            : 'Fokus Tata Kelola & Regulasi Nasional';
        }}
      }},

      setFontScale(scale) {{
        document.documentElement.style.setProperty('--app-font-scale', scale);
        document.querySelectorAll('.font-scale-btn').forEach(btn => btn.classList.remove('active'));
        if (scale === '90%') document.getElementById('fScaleSm')?.classList.add('active');
        else if (scale === '100%') document.getElementById('fScaleMd')?.classList.add('active');
        else if (scale === '115%') document.getElementById('fScaleLg')?.classList.add('active');
      }},

      navigate(viewName) {{
        document.getElementById('viewHome').style.display = viewName === 'home' ? 'block' : 'none';
        document.getElementById('viewPracticeConfig').style.display = viewName === 'practice-config' ? 'block' : 'none';
        document.getElementById('viewExam').style.display = viewName === 'exam' ? 'block' : 'none';
        document.getElementById('viewResults').style.display = viewName === 'results' ? 'block' : 'none';
        document.getElementById('viewGlossary').style.display = viewName === 'glossary' ? 'block' : 'none';
        document.getElementById('viewHistory').style.display = viewName === 'history' ? 'block' : 'none';

        if (viewName === 'history') {{
          this.renderHistoryView();
        }}

        window.scrollTo({{ top: 0, behavior: 'smooth' }});
      }},

      closeModals() {{
        document.querySelectorAll('.modal-backdrop').forEach(m => m.classList.remove('open'));
      }},

      readCandidateInputs() {{
        const nameInput = document.getElementById('inputCandidateName');
        const villageInput = document.getElementById('inputCandidateVillage');
        const regionInput = document.getElementById('selectRegion');

        this.candidateName = (nameInput && nameInput.value.trim()) ? nameInput.value.trim() : 'Peserta Ujian';
        this.candidateVillage = (villageInput && villageInput.value.trim()) ? villageInput.value.trim() : 'Desa Belum Ditentukan';
        this.region = regionInput ? regionInput.value : 'tuban';
      }},

      // ======================================================================
      // EXAM LAUNCH & TIMERS
      // ======================================================================
      confirmStartExam() {{
        this.readCandidateInputs();
        document.getElementById('modalStartExam').classList.add('open');
      }},

      startExamNow() {{
        this.closeModals();
        this.readCandidateInputs();
        this.mode = 'exam';
        this.examSubmitted = false;

        // Otomatis acak 100 soal dan acak pilihan jawaban A, B, C, D (Anti-Kecurangan Aktif)
        this.questions = generateExam100Questions(MASTER_QUESTIONS, CATEGORIES_SPEC, true, true);
        this.userAnswers = {{}};
        this.flaggedQuestions = {{}};
        this.visitedCount = {{}};
        this.currentIndex = 0;
        this.inPriorityCycle = false;

        this.examStartTime = Date.now();
        this.questionVisitStartTime = Date.now();
        this.isExamRunning = true;

        this.updateCandidateHeaderUI();
        this.renderQuestionPaletteGrid();
        this.renderCurrentQuestion();
        this.startTimerTickLoop();
        this.saveSession();

        this.navigate('exam');
      }},

      startPracticeSession() {{
        this.readCandidateInputs();
        this.mode = 'practice';
        this.examSubmitted = false;

        const catSelect = document.getElementById('practiceCategorySelect');
        const countSelect = document.getElementById('practiceCountSelect');
        const shuffleSelect = document.getElementById('practiceShuffleSelect');
        const timerToggle = document.getElementById('practiceTimerToggle');

        const selectedCat = catSelect ? catSelect.value : 'all';
        const count = countSelect ? parseInt(countSelect.value, 10) : 25;
        const doShuffle = shuffleSelect ? shuffleSelect.value === 'yes' : true;
        const useTimer = timerToggle ? timerToggle.checked : false;

        let selected = [];
        if (selectedCat === 'all' && count === 100) {{
          selected = generateExam100Questions(MASTER_QUESTIONS, CATEGORIES_SPEC, doShuffle, doShuffle);
        }} else {{
          let pool = [...MASTER_QUESTIONS];
          if (selectedCat !== 'all') {{
            pool = pool.filter(q => q.category === selectedCat);
          }}
          if (doShuffle) shuffleArray(pool);
          const picked = pool.slice(0, Math.min(pool.length, count));
          selected = picked.map((q, idx) => {{
            const origCorrect = q.options[q.answer];
            const opts = [...q.options];
            if (doShuffle) shuffleArray(opts);
            return {{
              ...q,
              number: idx + 1,
              options: opts,
              answer: opts.indexOf(origCorrect)
            }};
          }});
        }}

        this.questions = selected;
        this.currentIndex = 0;
        this.userAnswers = {{}};
        this.flaggedQuestions = {{}};
        this.visitedCount = {{}};
        this.examStartTime = Date.now();
        this.questionVisitStartTime = Date.now();
        this.isExamRunning = true;

        document.getElementById('boxTotalTimer').style.display = useTimer ? 'flex' : 'none';
        document.getElementById('boxQuestionTimer').style.display = useTimer ? 'flex' : 'none';

        this.updateCandidateHeaderUI();
        this.renderQuestionPaletteGrid();
        this.renderCurrentQuestion();
        if (useTimer) this.startTimerTickLoop();

        this.navigate('exam');
      }},

      startAdaptiveDrill(drillType) {{
        this.closeModals();
        this.readCandidateInputs();
        
        let pool = [];
        if (drillType === 'wrong') {{
          // Filter wrong questions from last evaluation or sample
          if (this.lastEvaluationData) {{
            pool = this.lastEvaluationData.filter(i => i.status === 'wrong');
          }}
        }} else if (drillType === 'empty') {{
          if (this.lastEvaluationData) {{
            pool = this.lastEvaluationData.filter(i => i.status === 'empty');
          }}
        }} else if (drillType === 'flagged') {{
          if (this.lastEvaluationData) {{
            pool = this.lastEvaluationData.filter(i => this.flaggedQuestions[i.id]);
          }}
        }}

        if (!pool || pool.length === 0) {{
          alert('Tidak ada butir soal yang sesuai untuk latihan adaptif ini pada sesi terakhir. Memuat latihan acak 10 soal...');
          pool = shuffleArray([...MASTER_QUESTIONS]).slice(0, 10);
        }}

        this.mode = 'practice';
        this.examSubmitted = false;
        this.questions = pool.map((q, idx) => ({{
          ...q,
          number: idx + 1,
          options: [...q.options]
        }}));

        this.currentIndex = 0;
        this.userAnswers = {{}};
        this.flaggedQuestions = {{}};
        this.visitedCount = {{}};
        this.examStartTime = Date.now();
        this.questionVisitStartTime = Date.now();
        this.isExamRunning = true;

        document.getElementById('boxTotalTimer').style.display = 'none';
        document.getElementById('boxQuestionTimer').style.display = 'none';

        this.updateCandidateHeaderUI();
        this.renderQuestionPaletteGrid();
        this.renderCurrentQuestion();
        this.navigate('exam');
      }},

      startAdaptiveCategory(catName) {{
        const pool = MASTER_QUESTIONS.filter(q => q.category === catName);
        this.questions = shuffleArray([...pool]).map((q, idx) => ({{
          ...q,
          number: idx + 1,
          options: [...q.options]
        }}));
        this.mode = 'practice';
        this.examSubmitted = false;
        this.currentIndex = 0;
        this.userAnswers = {{}};
        this.flaggedQuestions = {{}};
        this.visitedCount = {{}};
        this.examStartTime = Date.now();
        this.questionVisitStartTime = Date.now();
        this.isExamRunning = true;

        document.getElementById('boxTotalTimer').style.display = 'none';
        document.getElementById('boxQuestionTimer').style.display = 'none';

        this.updateCandidateHeaderUI();
        this.renderQuestionPaletteGrid();
        this.renderCurrentQuestion();
        this.navigate('exam');
      }},

      startAdaptiveFromResults(statusType) {{
        if (!this.lastEvaluationData) return;
        const filtered = this.lastEvaluationData.filter(i => i.status === statusType);
        if (filtered.length === 0) {{
          alert('Tidak ada soal berstatus ' + statusType + ' pada ujian ini.');
          return;
        }}
        this.questions = filtered.map((q, idx) => ({{
          ...q,
          number: idx + 1,
          options: [...q.options]
        }}));
        this.mode = 'practice';
        this.examSubmitted = false;
        this.currentIndex = 0;
        this.userAnswers = {{}};
        this.flaggedQuestions = {{}};
        this.visitedCount = {{}};
        this.isExamRunning = true;

        document.getElementById('boxTotalTimer').style.display = 'none';
        document.getElementById('boxQuestionTimer').style.display = 'none';

        this.updateCandidateHeaderUI();
        this.renderQuestionPaletteGrid();
        this.renderCurrentQuestion();
        this.navigate('exam');
      }},

      openAdaptiveModal() {{
        document.getElementById('modalAdaptiveChoice').classList.add('open');
      }},

      updateCandidateHeaderUI() {{
        const avatar = document.getElementById('avatarInitial');
        const nameEl = document.getElementById('barCandidateName');
        const regionEl = document.getElementById('barRegionBadge');
        const modeEl = document.getElementById('barModeBadge');

        if (avatar) avatar.textContent = this.candidateName.charAt(0).toUpperCase();
        if (nameEl) nameEl.textContent = this.candidateName;
        if (regionEl) regionEl.textContent = this.region === 'tuban' ? 'Kabupaten Tuban' : 'Standar Nasional';
        if (modeEl) modeEl.textContent = this.mode === 'exam' ? 'Simulasi CAT (100 Menit)' : 'Mode Latihan Belajar';
      }},

      startTimerTickLoop() {{
        if (this.timerInterval) clearInterval(this.timerInterval);
        this.timerInterval = setInterval(() => {{
          if (!this.isExamRunning) return;
          this.onTimerTick();
        }}, 250);
      }},

      onTimerTick() {{
        const now = Date.now();
        const totalElapsed = now - this.examStartTime;
        const totalRemaining = Math.max(0, this.examDurationMs - totalElapsed);

        if (totalRemaining <= 0) {{
          this.finishExam('TIME_EXPIRED');
          return;
        }}

        const totMins = Math.floor(totalRemaining / 60000);
        const totSecs = Math.floor((totalRemaining % 60000) / 1000);
        const dispTotal = document.getElementById('displayTotalTimer');
        const boxTotal = document.getElementById('boxTotalTimer');
        if (dispTotal) {{
          dispTotal.textContent = `${{totMins.toString().padStart(2, '0')}}:${{totSecs.toString().padStart(2, '0')}}`;
        }}
        if (boxTotal) {{
          if (totalRemaining < 5 * 60 * 1000) boxTotal.classList.add('urgent');
          else boxTotal.classList.remove('urgent');
        }}

        // Question timer (60s)
        const qElapsed = now - this.questionVisitStartTime;
        const qRemaining = Math.max(0, Math.min(totalRemaining, this.questionDurationMs - qElapsed));
        const qSecs = Math.ceil(qRemaining / 1000);
        const dispQ = document.getElementById('displayQuestionTimer');
        const boxQ = document.getElementById('boxQuestionTimer');
        if (dispQ) dispQ.textContent = `${{qSecs}}s`;
        if (boxQ) {{
          if (qRemaining <= 10000) boxQ.classList.add('urgent');
          else boxQ.classList.remove('urgent');
        }}

        if (qRemaining <= 0) {{
          this.onQuestionTimeoutAutoAdvance();
        }}
      }},

      onQuestionTimeoutAutoAdvance() {{
        const currentQ = this.questions[this.currentIndex];
        this.visitedCount[currentQ.id] = (this.visitedCount[currentQ.id] || 0) + 1;
        this.advanceToNextAutoPriority();
      }},

      advanceToNextAutoPriority() {{
        if (this.isAllAnswered()) {{
          this.confirmFinishExam();
          return;
        }}

        if (!this.inPriorityCycle) {{
          // Sequential forward pass
          let nextIndex = -1;
          for (let i = this.currentIndex + 1; i < this.questions.length; i++) {{
            if (this.userAnswers[this.questions[i].id] === undefined) {{
              nextIndex = i;
              break;
            }}
          }}

          if (nextIndex !== -1) {{
            this.goToQuestion(nextIndex);
            return;
          }} else {{
            this.inPriorityCycle = true;
          }}
        }}

        // Priority pass: lowest unanswered
        let lowest = -1;
        for (let i = 0; i < this.questions.length; i++) {{
          if (this.userAnswers[this.questions[i].id] === undefined) {{
            lowest = i;
            break;
          }}
        }}

        if (lowest !== -1) {{
          this.goToQuestion(lowest);
        }} else {{
          this.confirmFinishExam();
        }}
      }},

      isAllAnswered() {{
        return this.questions.length > 0 && this.questions.every(q => this.userAnswers[q.id] !== undefined);
      }},

      goToQuestion(targetIndex) {{
        if (targetIndex < 0 || targetIndex >= this.questions.length) return;
        this.currentIndex = targetIndex;
        this.questionVisitStartTime = Date.now();
        this.renderCurrentQuestion();
        this.renderQuestionPaletteGrid();
        this.saveSession();
      }},

      prevQuestion() {{
        if (this.currentIndex > 0) {{
          this.goToQuestion(this.currentIndex - 1);
        }}
      }},

      skipOrNextQuestion() {{
        const currentQ = this.questions[this.currentIndex];
        this.visitedCount[currentQ.id] = (this.visitedCount[currentQ.id] || 0) + 1;
        this.advanceToNextAutoPriority();
      }},

      toggleFlagCurrentQuestion() {{
        const q = this.questions[this.currentIndex];
        if (!q) return;
        this.flaggedQuestions[q.id] = !this.flaggedQuestions[q.id];
        this.renderCurrentQuestion();
        this.renderQuestionPaletteGrid();
        this.saveSession();
      }},

      renderCurrentQuestion() {{
        const q = this.questions[this.currentIndex];
        if (!q) return;

        const qIdxEl = document.getElementById('qDisplayIndex');
        const catEl = document.getElementById('qCategoryPill');
        const diffEl = document.getElementById('qDifficultyPill');
        const roundPill = document.getElementById('qRoundPill');
        const textEl = document.getElementById('qQuestionText');
        const optionsContainer = document.getElementById('qOptionsList');
        const flagBtn = document.getElementById('btnFlagQuestion');
        const flagLabel = document.getElementById('btnFlagLabel');

        if (qIdxEl) qIdxEl.textContent = `Soal Nomor ${{q.number || (this.currentIndex + 1)}} dari ${{this.questions.length}}`;
        if (catEl) catEl.textContent = q.category;
        if (diffEl) {{
          diffEl.textContent = (q.difficulty || 'SEDANG').toUpperCase();
          diffEl.className = `badge-pill badge-diff-${{q.difficulty || 'sedang'}}`;
        }}
        if (roundPill) {{
          roundPill.style.display = this.inPriorityCycle ? 'inline-flex' : 'none';
        }}
        if (textEl) textEl.textContent = q.question;

        const isFlagged = !!this.flaggedQuestions[q.id];
        if (flagBtn) {{
          if (isFlagged) {{
            flagBtn.classList.add('btn-flagged');
            if (flagLabel) flagLabel.textContent = 'Ragu-ragu (Aktif)';
          }} else {{
            flagBtn.classList.remove('btn-flagged');
            if (flagLabel) flagLabel.textContent = 'Ragu-ragu (R)';
          }}
        }}

        // Render Options
        const letters = ['A', 'B', 'C', 'D'];
        const selectedAnswer = this.userAnswers[q.id];
        let optionsHtml = '';

        q.options.forEach((optText, optIdx) => {{
          const isSelected = selectedAnswer === optIdx;
          let optClass = 'option-item';
          if (isSelected) optClass += ' selected';

          if (this.mode === 'practice' && selectedAnswer !== undefined) {{
            if (optIdx === q.answer) optClass += ' eval-correct';
            else if (isSelected && optIdx !== q.answer) optClass += ' eval-wrong';
          }}

          optionsHtml += `
            <div class="${{optClass}}" onclick="CBTApp.selectOption(${{optIdx}})" id="optBtn_${{optIdx}}">
              <div class="option-letter">${{letters[optIdx]}}</div>
              <div class="option-content">${{optText}}</div>
            </div>
          `;
        }});

        if (optionsContainer) optionsContainer.innerHTML = optionsHtml;

        // Practice feedback box
        const pBox = document.getElementById('practiceFeedbackBox');
        if (this.mode === 'practice' && selectedAnswer !== undefined) {{
          if (pBox) {{
            pBox.style.display = 'block';
            document.getElementById('practiceFeedbackContent').textContent = q.explanation;
            document.getElementById('practiceFeedbackSource').innerHTML = `<strong>Rujukan:</strong> ${{q.source}}`;
          }}
        }} else if (pBox) {{
          pBox.style.display = 'none';
        }}

        const prevBtn = document.getElementById('btnPrevQuestion');
        if (prevBtn) prevBtn.disabled = this.currentIndex === 0;
      }},

      selectOption(optionIndex) {{
        if (this.examSubmitted) return;
        const currentQ = this.questions[this.currentIndex];
        this.userAnswers[currentQ.id] = optionIndex;
        this.saveSession();

        if (this.mode === 'exam') {{
          this.renderQuestionPaletteGrid();
          this.advanceToNextAutoPriority();
        }} else {{
          this.renderCurrentQuestion();
          this.renderQuestionPaletteGrid();
        }}
      }},

      setPaletteFilter(filterType) {{
        this.paletteFilter = filterType;
        document.querySelectorAll('.palette-filter-btn').forEach(b => b.classList.remove('active'));
        if (filterType === 'all') document.getElementById('pFilterAll')?.classList.add('active');
        else if (filterType === 'done') document.getElementById('pFilterDone')?.classList.add('active');
        else if (filterType === 'flag') document.getElementById('pFilterFlag')?.classList.add('active');
        else if (filterType === 'empty') document.getElementById('pFilterEmpty')?.classList.add('active');
        this.renderQuestionPaletteGrid();
      }},

      renderQuestionPaletteGrid() {{
        const container = document.getElementById('gridQuestionButtons');
        if (!container) return;

        let answeredCount = 0;
        let html = '';

        this.questions.forEach((q, idx) => {{
          const isAnswered = this.userAnswers[q.id] !== undefined;
          const isFlagged = !!this.flaggedQuestions[q.id];
          const isCurrent = idx === this.currentIndex;

          if (isAnswered) answeredCount++;

          // Apply palette filter
          if (this.paletteFilter === 'done' && !isAnswered) return;
          if (this.paletteFilter === 'flag' && !isFlagged) return;
          if (this.paletteFilter === 'empty' && isAnswered) return;

          let btnClass = 'btn-palette-num';
          if (isAnswered) btnClass += ' answered';
          if (isFlagged) btnClass += ' flagged';
          if (isCurrent) btnClass += ' active';

          html += `
            <button class="${{btnClass}}" onclick="CBTApp.goToQuestion(${{idx}})" title="Soal ${{idx + 1}}">
              ${{idx + 1}}
            </button>
          `;
        }});

        container.innerHTML = html;
        const counterEl = document.getElementById('paletteAnswerCount');
        if (counterEl) counterEl.textContent = `Terjawab: ${{answeredCount}} / ${{this.questions.length}}`;
      }},

      // Pre-Finish Modal (Feature 1)
      confirmFinishExam() {{
        const total = this.questions.length;
        let answered = 0;
        let flagged = 0;
        let empty = 0;
        let emptyIndices = [];
        let flaggedIndices = [];

        this.questions.forEach((q, idx) => {{
          const isAns = this.userAnswers[q.id] !== undefined;
          const isFlag = !!this.flaggedQuestions[q.id];
          if (isAns) answered++;
          else {{
            empty++;
            emptyIndices.push(idx);
          }}
          if (isFlag) flaggedIndices.push(idx);
        }});

        document.getElementById('preFinishAnswered').textContent = answered;
        document.getElementById('preFinishFlagged').textContent = flaggedIndices.length;
        document.getElementById('preFinishEmpty').textContent = empty;

        const warnBox = document.getElementById('preFinishWarningBox');
        let warnHtml = '';
        if (empty > 0) {{
          warnHtml += `
            <div style="background:var(--rose-50); border:1px solid var(--rose-400); color:var(--rose-800); padding:0.75rem; border-radius:var(--radius-sm); font-size:0.85rem; margin-bottom:0.5rem;">
              <strong>PERINGATAN:</strong> Masih ada <strong>${{empty}} butir soal yang belum dijawab</strong>! Pada CAT perangkat desa, soal kosong bernilai 0 dan tidak ada pengurangan nilai untuk jawaban salah. Anda disarankan menjawab seluruh soal.
            </div>
          `;
        }}
        if (flaggedIndices.length > 0) {{
          warnHtml += `
            <div style="background:var(--accent-gold-50); border:1px solid var(--accent-gold-400); color:var(--accent-gold-800); padding:0.75rem; border-radius:var(--radius-sm); font-size:0.85rem;">
              <strong>CATATAN:</strong> Ada <strong>${{flaggedIndices.length}} soal yang ditandai ragu-ragu</strong>. Jawaban yang telah dipilih tetap dinilai, namun Anda disarankan memeriksanya kembali.
            </div>
          `;
        }}
        if (warnBox) warnBox.innerHTML = warnHtml;

        const jumpWrap = document.getElementById('preFinishJumpWrap');
        const jumpChips = document.getElementById('preFinishJumpChips');
        if (emptyIndices.length > 0 || flaggedIndices.length > 0) {{
          if (jumpWrap) jumpWrap.style.display = 'block';
          let chipsHtml = '';
          emptyIndices.forEach(idx => {{
            chipsHtml += `<span class="jump-chip" onclick="CBTApp.closeModals(); CBTApp.goToQuestion(${{idx}});" style="color:var(--rose-700);">No. ${{idx + 1}} (Kosong)</span>`;
          }});
          flaggedIndices.forEach(idx => {{
            chipsHtml += `<span class="jump-chip" onclick="CBTApp.closeModals(); CBTApp.goToQuestion(${{idx}});" style="color:var(--accent-gold-700);">No. ${{idx + 1}} (Ragu)</span>`;
          }});
          if (jumpChips) jumpChips.innerHTML = chipsHtml;
        }} else if (jumpWrap) {{
          jumpWrap.style.display = 'none';
        }}

        document.getElementById('modalFinishExam').classList.add('open');
      }},

      finishExam(reason) {{
        this.closeModals();
        this.isExamRunning = false;
        this.examSubmitted = true;
        if (this.timerInterval) clearInterval(this.timerInterval);

        if (reason === 'TIME_EXPIRED') {{
          document.getElementById('modalTimeExpired').classList.add('open');
        }} else {{
          this.showResultsView();
        }}

        safeSetStorage(this.STORAGE_KEY, null);
      }},

      // ======================================================================
      // RESULTS VIEW, WEAKNESS ANALYSIS & HISTORY (FEATURES 2 & 5)
      // ======================================================================
      showResultsView() {{
        const totalSoal = this.questions.length;
        let countBenar = 0;
        let countSalah = 0;
        let countKosong = 0;

        const catStats = {{}};
        CATEGORIES_SPEC.forEach(c => {{
          catStats[c.name] = {{ total: 0, correct: 0, wrong: 0, empty: 0 }};
        }});

        this.evaluationData = this.questions.map((q, idx) => {{
          const userAns = this.userAnswers[q.id];
          const isAnswered = userAns !== undefined;
          const isCorrect = isAnswered && userAns === q.answer;

          if (!catStats[q.category]) {{
            catStats[q.category] = {{ total: 0, correct: 0, wrong: 0, empty: 0 }};
          }}
          catStats[q.category].total++;

          if (!isAnswered) {{
            countKosong++;
            catStats[q.category].empty++;
          }} else if (isCorrect) {{
            countBenar++;
            catStats[q.category].correct++;
          }} else {{
            countSalah++;
            catStats[q.category].wrong++;
          }}

          return {{
            id: q.id,
            number: idx + 1,
            category: q.category,
            difficulty: q.difficulty,
            question: q.question,
            options: q.options,
            keyAnswer: q.answer,
            userAnswer: userAns,
            isAnswered,
            isCorrect,
            status: !isAnswered ? 'empty' : (isCorrect ? 'correct' : 'wrong'),
            explanation: q.explanation,
            source: q.source
          }};
        }});

        this.lastEvaluationData = this.evaluationData;

        const finalScore = totalSoal > 0 ? (countBenar / totalSoal) * 100 : 0;
        const accuracy = totalSoal > 0 ? ((countBenar / totalSoal) * 100).toFixed(1) : 0;
        const totalElapsedMs = Math.min(this.examDurationMs, Date.now() - (this.examStartTime || Date.now()));
        const elapsedMinutes = Math.floor(totalElapsedMs / 60000);
        const elapsedSeconds = Math.floor((totalElapsedMs % 60000) / 1000);
        const timeUsedStr = `${{elapsedMinutes}} Menit ${{elapsedSeconds}} Detik`;

        document.getElementById('resCandidateHeading').textContent = `Hasil Simulasi Ujian: ${{this.candidateName}}`;
        document.getElementById('resCandidateSubheading').textContent = `${{this.candidateVillage}} • ${{this.region === 'tuban' ? 'Kabupaten Tuban, Jatim' : 'Standar Nasional'}}`;
        document.getElementById('resBadgeMode').textContent = this.mode === 'exam' ? 'Simulasi CAT (100 Menit)' : 'Mode Latihan Belajar';
        document.getElementById('resBadgeRegion').textContent = this.region === 'tuban' ? 'Kabupaten Tuban' : 'Standar Nasional';
        document.getElementById('resDateBadge').textContent = new Date().toLocaleDateString('id-ID', {{ day: 'numeric', month: 'long', year: 'numeric' }});

        document.getElementById('resTotalSoal').textContent = totalSoal;
        document.getElementById('resCountBenar').textContent = countBenar;
        document.getElementById('resCountSalah').textContent = countSalah;
        document.getElementById('resCountKosong').textContent = countKosong;
        document.getElementById('resTimeUsed').textContent = timeUsedStr;

        document.getElementById('resScoreValue').textContent = finalScore.toFixed(0);
        document.getElementById('resAccuracyPercent').textContent = `${{accuracy}}%`;

        // Render Weakness Analysis & Category Breakdown
        this.renderWeaknessAnalysis(catStats);
        this.renderResultsCategoryTable(catStats);
        this.renderActiveReviewTab();

        // Save to History (Feature 5)
        this.saveExamToHistory({{
          id: 'sesi_' + Date.now(),
          timestamp: Date.now(),
          dateFormatted: new Date().toLocaleDateString('id-ID', {{ day: 'numeric', month: 'short', year: 'numeric', hour: '2-digit', minute: '2-digit' }}),
          candidateName: this.candidateName,
          mode: this.mode,
          modeLabel: this.mode === 'exam' ? 'Simulasi CAT (100 Menit)' : 'Mode Latihan',
          isOfficialExam: this.mode === 'exam' && totalSoal === 100,
          totalQuestions: totalSoal,
          correct: countBenar,
          wrong: countSalah,
          empty: countKosong,
          score: finalScore,
          accuracy: parseFloat(accuracy),
          timeUsedFormatted: timeUsedStr
        }});

        this.navigate('results');
      }},

      renderWeaknessAnalysis(catStats) {{
        const container = document.getElementById('weaknessListContainer');
        if (!container) return;

        const catArray = Object.keys(catStats).map(catName => {{
          const st = catStats[catName];
          const acc = st.total > 0 ? (st.correct / st.total) * 100 : 0;
          return {{ name: catName, ...st, acc: parseFloat(acc.toFixed(1)) }};
        }}).filter(c => c.total > 0);

        // Sort ascending by accuracy (weakest first)
        catArray.sort((a, b) => a.acc - b.acc);

        let html = '';
        catArray.forEach(cat => {{
          let cardClass = 'weakness-card';
          let badge = '';
          let fillClass = 'background:var(--rose-600);';
          let advice = '';

          if (cat.acc < 50) {{
            cardClass += ' needs-work';
            badge = '<span class="badge-pill badge-diff-sulit">PERLU PENDALAMAN SERIUS</span>';
            fillClass = 'background:var(--rose-600);';
            advice = `Pelajari kembali regulasi dan ketentuan pasal rujukan untuk kategori ini. Sangat dianjurkan melakukan latihan khusus.`;
          }} else if (cat.acc < 70) {{
            cardClass += ' fair';
            badge = '<span class="badge-pill badge-diff-sedang">CUKUP - PERLU PENGUATAN</span>';
            fillClass = 'background:var(--accent-gold-500);';
            advice = `Penguasaan materi sudah lumayan, perbanyak latihan soal kasus dan analisis tata kelola.`;
          }} else {{
            cardClass += ' mastered';
            badge = '<span class="badge-pill badge-diff-mudah">MENGUASAI DENGAN BAIK</span>';
            fillClass = 'background:var(--emerald-600);';
            advice = `Pertahankan pemahaman Anda pada kategori ini.`;
          }}

          html += `
            <div class="${{cardClass}}">
              <div class="weakness-header">
                <div style="font-weight:800; font-size:1rem; color:var(--primary-900);">${{cat.name}}</div>
                <div>${{badge}}</div>
              </div>
              <div style="display:flex; justify-content:space-between; font-size:0.82rem; color:var(--slate-600);">
                <span>Benar: ${{cat.correct}} dari ${{cat.total}} soal</span>
                <span style="font-weight:700;">Akurasi: ${{cat.acc}}%</span>
              </div>
              <div class="progress-bar-wrap">
                <div class="progress-bar-fill" style="width:${{cat.acc}}%; ${{fillClass}}"></div>
              </div>
              <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.5rem; margin-top:0.25rem;">
                <p style="font-size:0.82rem; color:var(--slate-600);">${{advice}}</p>
                <button class="btn btn-outline btn-sm" onclick="CBTApp.startAdaptiveCategory('${{cat.name}}')">Latihan Kategori Ini</button>
              </div>
            </div>
          `;
        }});

        container.innerHTML = html;
      }},

      renderResultsCategoryTable(catStats) {{
        const tbody = document.getElementById('resultsCategoryTableBody');
        if (!tbody) return;
        let html = '';
        let no = 1;

        for (const [catName, st] of Object.entries(catStats)) {{
          if (st.total === 0) continue;
          const acc = ((st.correct / st.total) * 100).toFixed(1);
          let statusBadge = '<span class="badge-pill badge-diff-mudah">Menguasai</span>';
          if (acc < 50) statusBadge = '<span class="badge-pill badge-diff-sulit">Kurang</span>';
          else if (acc < 70) statusBadge = '<span class="badge-pill badge-diff-sedang">Cukup</span>';

          html += `
            <tr>
              <td style="text-align:center; font-weight:700; color:var(--slate-500);">${{no++}}</td>
              <td style="font-weight:600; color:var(--primary-900);">${{catName}}</td>
              <td style="text-align:center; font-weight:700;">${{st.total}}</td>
              <td style="text-align:center; font-weight:700; color:var(--emerald-600);">${{st.correct}}</td>
              <td style="text-align:center; font-weight:700; color:var(--rose-600);">${{st.wrong}}</td>
              <td style="text-align:center; font-weight:700; color:var(--slate-500);">${{st.empty}}</td>
              <td style="text-align:center; font-weight:700;">${{acc}}%</td>
              <td>${{statusBadge}}</td>
            </tr>
          `;
        }}
        tbody.innerHTML = html;
      }},

      setReviewTab(tabType) {{
        this.activeReviewTab = tabType;
        document.querySelectorAll('#tabRevWrong, #tabRevEmpty, #tabRevCorrect, #tabRevAll').forEach(b => b.classList.remove('active'));
        if (tabType === 'wrong') document.getElementById('tabRevWrong')?.classList.add('active');
        else if (tabType === 'empty') document.getElementById('tabRevEmpty')?.classList.add('active');
        else if (tabType === 'correct') document.getElementById('tabRevCorrect')?.classList.add('active');
        else if (tabType === 'all') document.getElementById('tabRevAll')?.classList.add('active');
        this.renderActiveReviewTab();
      }},

      renderActiveReviewTab() {{
        const container = document.getElementById('evalReviewContainer');
        if (!container || !this.evaluationData) return;

        const keyword = (document.getElementById('reviewSearchInput')?.value || '').toLowerCase().trim();
        let filtered = this.evaluationData.filter(item => {{
          if (this.activeReviewTab === 'wrong' && item.status !== 'wrong') return false;
          if (this.activeReviewTab === 'empty' && item.status !== 'empty') return false;
          if (this.activeReviewTab === 'correct' && item.status !== 'correct') return false;

          if (keyword) {{
            const matchQ = item.question.toLowerCase().includes(keyword);
            const matchExp = item.explanation.toLowerCase().includes(keyword);
            const matchSrc = item.source.toLowerCase().includes(keyword);
            if (!matchQ && !matchExp && !matchSrc) return false;
          }}
          return true;
        }});

        if (filtered.length === 0) {{
          container.innerHTML = `
            <div style="text-align:center; padding:2rem 1rem; color:var(--slate-600);">
              Tidak ada butir soal yang sesuai dengan kriteria tab ini.
            </div>
          `;
          return;
        }}

        const letters = ['A', 'B', 'C', 'D'];
        let html = '';

        filtered.forEach(item => {{
          let cardClass = 'review-item-card is-' + item.status;
          let statusBadge = item.status === 'correct'
            ? '<span class="badge-pill badge-diff-mudah">✓ BENAR (+1)</span>'
            : (item.status === 'wrong' 
                ? '<span class="badge-pill badge-diff-sulit">✗ SALAH (0)</span>'
                : '<span class="badge-pill" style="background:var(--slate-200); color:var(--slate-700);">○ KOSONG (0)</span>');

          const userAnsText = item.isAnswered ? `${{letters[item.userAnswer]}}. ${{item.options[item.userAnswer]}}` : '(Tidak Dijawab)';
          const keyAnsText = `${{letters[item.keyAnswer]}}. ${{item.options[item.keyAnswer]}}`;

          html += `
            <div class="${{cardClass}}">
              <div class="question-meta-row" style="margin-bottom:0.75rem;">
                <div style="font-weight:800; font-size:1rem; color:var(--primary-900);">Soal Nomor ${{item.number}}</div>
                <div class="badges-group">
                  <span class="badge-pill badge-cat">${{item.category}}</span>
                  ${{statusBadge}}
                </div>
              </div>

              <div class="question-text" style="font-size:1rem; margin-bottom:1rem;">${{item.question}}</div>

              <div style="display:grid; grid-template-columns:1fr 1fr; gap:0.75rem; margin-bottom:0.75rem; font-size:0.88rem;">
                <div style="background:var(--slate-50); padding:0.6rem 0.85rem; border-radius:var(--radius-sm); border:1px solid var(--slate-200);">
                  <strong style="color:var(--slate-700);">Jawaban Anda:</strong>
                  <div style="color:${{item.isCorrect ? 'var(--emerald-700)' : 'var(--rose-700)'}}; font-weight:700;">${{userAnsText}}</div>
                </div>
                <div style="background:var(--emerald-50); padding:0.6rem 0.85rem; border-radius:var(--radius-sm); border:1px solid var(--emerald-300);">
                  <strong style="color:var(--emerald-800);">Kunci Benar:</strong>
                  <div style="color:var(--emerald-800); font-weight:700;">${{keyAnsText}}</div>
                </div>
              </div>

              <div class="explanation-box">
                <div style="font-weight:700; color:var(--primary-800); margin-bottom:0.25rem;">Pembahasan Regulasi:</div>
                <div>${{item.explanation}}</div>
                <div class="explanation-source"><strong>Dasar Hukum:</strong> ${{item.source}}</div>
              </div>
            </div>
          `;
        }});

        container.innerHTML = html;
      }},

      // ======================================================================
      // GLOSSARY ENGINE (FEATURE 4)
      // ======================================================================
      renderGlossary() {{
        const container = document.getElementById('glossaryListContainer');
        if (!container) return;

        const keyword = (document.getElementById('glossarySearchInput')?.value || '').toLowerCase().trim();
        const selectedCat = document.getElementById('glossaryCategorySelect')?.value || 'all';

        const filtered = GLOSSARY_DATA.filter(item => {{
          if (selectedCat !== 'all' && item.category !== selectedCat) return false;
          if (keyword) {{
            const matchTerm = item.term.toLowerCase().includes(keyword);
            const matchName = item.name.toLowerCase().includes(keyword);
            const matchDef = item.definition.toLowerCase().includes(keyword);
            const matchSrc = item.source.toLowerCase().includes(keyword);
            if (!matchTerm && !matchName && !matchDef && !matchSrc) return false;
          }}
          return true;
        }});

        if (filtered.length === 0) {{
          container.innerHTML = `
            <div style="grid-column:1/-1; text-align:center; padding:2rem; color:var(--slate-500);">
              Tidak ada istilah yang cocok dengan kata kunci "${{keyword}}".
            </div>
          `;
          return;
        }}

        let html = '';
        filtered.forEach(item => {{
          html += `
            <div class="glossary-card">
              <div>
                <div style="display:flex; justify-content:space-between; align-items:flex-start; gap:0.5rem; margin-bottom:0.35rem;">
                  <div class="glossary-term">${{item.term}}</div>
                  <span class="badge-pill badge-cat" style="font-size:0.7rem;">${{item.category}}</span>
                </div>
                <div style="font-weight:700; font-size:0.9rem; color:var(--slate-800); margin-bottom:0.5rem;">${{item.name}}</div>
                <div class="glossary-def">${{item.definition}}</div>
              </div>
              <div class="glossary-src">
                <strong>Rujukan:</strong> ${{item.source}}
              </div>
            </div>
          `;
        }});

        container.innerHTML = html;
      }},

      // ======================================================================
      // HISTORY & PROGRESSION (FEATURE 5)
      // ======================================================================
      saveExamToHistory(sessionData) {{
        const history = safeGetStorage(this.HISTORY_KEY, []);
        history.unshift(sessionData);
        // Keep up to 30 latest sessions
        if (history.length > 30) history.pop();
        safeSetStorage(this.HISTORY_KEY, history);
      }},

      renderHistoryView() {{
        const history = safeGetStorage(this.HISTORY_KEY, []);
        const tbody = document.getElementById('historyTableBody');
        const compBox = document.getElementById('historyComparisonBox');
        const chartBox = document.getElementById('chartContainer');

        if (!tbody || !compBox || !chartBox) return;

        if (history.length === 0) {{
          compBox.innerHTML = `
            <div class="comparison-notice valid">
              Belum ada riwayat sesi yang tersimpan. Ikuti simulasi ujian atau latihan untuk memantau grafik perkembangan skor Anda.
            </div>
          `;
          chartBox.innerHTML = '<div style="text-align:center; padding:3rem; color:var(--slate-500);">Data grafik belum tersedia.</div>';
          tbody.innerHTML = '<tr><td colspan="9" style="text-align:center; padding:2rem; color:var(--slate-500);">Belum ada riwayat simulasi.</td></tr>';
          return;
        }}

        // Render Comparison Analysis (Feature 5 Requirement: Compare only equal sessions or give clear notice)
        let compHtml = '';
        if (history.length >= 2) {{
          const latest = history[0];
          const prev = history[1];

          if (latest.isOfficialExam && prev.isOfficialExam) {{
            const deltaScore = latest.score - prev.score;
            const deltaAcc = (latest.accuracy - prev.accuracy).toFixed(1);
            const trendIcon = deltaScore >= 0 ? '📈 Kenaikan Skor:' : '📉 Penurunan Skor:';
            compHtml = `
              <div class="comparison-notice valid">
                <div>
                  <strong>Komparasi Sesi Setara (Simulasi Resmi 100 Soal):</strong><br>
                  ${{trendIcon}} <strong>${{deltaScore >= 0 ? '+' : ''}}${{deltaScore.toFixed(0)}} poin</strong> (dari ${{prev.score.toFixed(0)}} ke ${{latest.score.toFixed(0)}}) • Selisih Akurasi: ${{deltaAcc >= 0 ? '+' : ''}}${{deltaAcc}}%.
                </div>
              </div>
            `;
          }} else {{
            compHtml = `
              <div class="comparison-notice disparate">
                <div>
                  <strong>Pemberitahuan Perbandingan Sesi:</strong> Sesi terakhir (${{latest.modeLabel}}, ${{latest.totalQuestions}} soal) memiliki cakupan atau jumlah butir berbeda dengan sesi sebelumnya (${{prev.modeLabel}}, ${{prev.totalQuestions}} soal). <em>Hasil tidak dapat disetarakan secara langsung sebagai indikator tren.</em>
                </div>
              </div>
            `;
          }}
        }} else {{
          compHtml = `
            <div class="comparison-notice valid">
              Sesi pertama Anda berhasil dicatat dengan skor <strong>${{history[0].score.toFixed(0)}}</strong>. Ikuti sesi berikutnya untuk melihat grafik tren kenaikan nilai.
            </div>
          `;
        }}
        compBox.innerHTML = compHtml;

        // Render SVG Line Chart
        this.renderHistoryChart(history, chartBox);

        // Render Table
        let tableHtml = '';
        history.forEach((h, idx) => {{
          tableHtml += `
            <tr>
              <td style="text-align:center; font-weight:700; color:var(--slate-500);">${{idx + 1}}</td>
              <td style="font-weight:600;">${{h.dateFormatted}}</td>
              <td>${{h.candidateName}}</td>
              <td><span class="badge-pill badge-cat">${{h.modeLabel}}</span></td>
              <td style="text-align:center; font-weight:700;">${{h.totalQuestions}}</td>
              <td style="text-align:center; font-weight:700; color:var(--emerald-600);">${{h.correct}}</td>
              <td style="text-align:center; font-weight:900; color:var(--primary-800);">${{h.score.toFixed(0)}}</td>
              <td style="text-align:center; font-weight:700;">${{h.accuracy}}%</td>
              <td style="font-size:0.8rem; color:var(--slate-600);">${{h.weakestCategory || '-'}}</td>
            </tr>
          `;
        }});
        tbody.innerHTML = tableHtml;
      }},

      renderHistoryChart(history, chartBox) {{
        // Take chronologically up to 10 latest sessions
        const rev = [...history].reverse().slice(-10);
        const w = 700;
        const h = 200;
        const padding = 35;

        if (rev.length === 1) {{
          chartBox.innerHTML = `
            <div style="text-align:center; padding:2.5rem; color:var(--slate-700);">
              Skor Sesi Pertama: <strong style="font-size:1.5rem; color:var(--emerald-700);">${{rev[0].score.toFixed(0)}}</strong> / 100.<br>
              Lakukan simulasi berikutnya untuk melihat garis tren nilai.
            </div>
          `;
          return;
        }}

        const stepX = (w - padding * 2) / (rev.length - 1);
        let points = [];
        rev.forEach((d, idx) => {{
          const x = padding + idx * stepX;
          const y = h - padding - (d.score / 100) * (h - padding * 2);
          points.push({{ x, y, score: d.score, date: d.dateFormatted, mode: d.modeLabel }});
        }});

        let polylinePoints = points.map(p => `${{p.x}},${{p.y}}`).join(' ');
        let circles = points.map(p => `
          <circle cx="${{p.x}}" cy="${{p.y}}" r="5" fill="#2563eb" stroke="#ffffff" stroke-width="2">
            <title>${{p.date}} - Skor: ${{p.score.toFixed(0)}} (${{p.mode}})</title>
          </circle>
          <text x="${{p.x}}" y="${{p.y - 10}}" font-size="10" font-weight="700" text-anchor="middle" fill="#1e3a8a">${{p.score.toFixed(0)}}</text>
        `).join('');

        chartBox.innerHTML = `
          <svg viewBox="0 0 ${{w}} ${{h}}" style="width:100%; height:100%; overflow:visible;">
            <!-- Grid lines -->
            <line x1="${{padding}}" y1="${{h - padding}}" x2="${{w - padding}}" y2="${{h - padding}}" stroke="#cbd5e1" stroke-width="1"/>
            <line x1="${{padding}}" y1="${{h - padding - (h - padding * 2) * 0.5}}" x2="${{w - padding}}" y2="${{h - padding - (h - padding * 2) * 0.5}}" stroke="#e2e8f0" stroke-width="1" stroke-dasharray="4"/>
            <line x1="${{padding}}" y1="${{padding}}" x2="${{w - padding}}" y2="${{padding}}" stroke="#e2e8f0" stroke-width="1" stroke-dasharray="4"/>
            
            <text x="${{padding - 5}}" y="${{h - padding + 4}}" font-size="9" text-anchor="end" fill="#64748b">0</text>
            <text x="${{padding - 5}}" y="${{h - padding - (h - padding * 2) * 0.5 + 3}}" font-size="9" text-anchor="end" fill="#64748b">50</text>
            <text x="${{padding - 5}}" y="${{padding + 3}}" font-size="9" text-anchor="end" fill="#64748b">100</text>

            <!-- Line Trend -->
            <polyline fill="none" stroke="#2563eb" stroke-width="3" points="${{polylinePoints}}" stroke-linecap="round" stroke-linejoin="round"/>
            ${{circles}}
          </svg>
        `;
      }},

      confirmClearHistory() {{
        if (confirm('Apakah Anda yakin ingin menghapus seluruh riwayat simulasi ujian Anda dari browser ini?')) {{
          safeSetStorage(this.HISTORY_KEY, []);
          this.renderHistoryView();
        }}
      }},

      // ======================================================================
      // LOCAL BACKUP & EXPORT/IMPORT JSON (FEATURE 8)
      // ======================================================================
      openBackupModal() {{
        document.getElementById('modalBackupRestore').classList.add('open');
      }},

      exportBackupJSON() {{
        const history = safeGetStorage(this.HISTORY_KEY, []);
        const backupData = {{
          app: "CBT_PERANGKAT_DESA",
          version: 2,
          exportDate: new Date().toISOString(),
          candidateProfile: {{
            name: this.candidateName,
            village: this.candidateVillage,
            region: this.region
          }},
          history: history
        }};

        const blob = new Blob([JSON.stringify(backupData, null, 2)], {{ type: 'application/json' }});
        this.downloadFile(blob, `CBT_Perangkat_Desa_Cadangan_${{Date.now()}}.json`);
      }},

      importBackupJSON(mode) {{
        const fileInput = document.getElementById('backupFileInput');
        if (!fileInput || !fileInput.files || fileInput.files.length === 0) {{
          alert('Silakan pilih file cadangan berformat .json terlebih dahulu.');
          return;
        }}

        const file = fileInput.files[0];
        // Enforce strict size check (max 2 MB)
        if (file.size > 2 * 1024 * 1024) {{
          alert('File cadangan terlalu besar! Batas maksimal ukuran file adalah 2 MB.');
          return;
        }}

        const reader = new FileReader();
        reader.onload = (e) => {{
          try {{
            const content = JSON.parse(e.target.result);
            // Strict Schema Validation
            if (!content || content.app !== "CBT_PERANGKAT_DESA" || !Array.isArray(content.history)) {{
              alert('File tidak valid! Format data cadangan tidak sesuai standar aplikasi CBT Perangkat Desa.');
              return;
            }}

            const currentHistory = safeGetStorage(this.HISTORY_KEY, []);
            let newHistory = [];

            if (mode === 'merge') {{
              // Merge without duplicates by ID
              const existingIds = new Set(currentHistory.map(h => h.id));
              newHistory = [...currentHistory];
              content.history.forEach(h => {{
                if (!existingIds.has(h.id)) {{
                  newHistory.push(h);
                }}
              }});
            }} else {{
              newHistory = content.history;
            }}

            // Sanitize history structure
            newHistory = newHistory.filter(h => h && typeof h.score === 'number' && h.dateFormatted);
            safeSetStorage(this.HISTORY_KEY, newHistory);

            alert(`Berhasil memulihkan ${{newHistory.length}} riwayat simulasi.`);
            this.closeModals();
            this.navigate('history');
          }} catch (err) {{
            alert('Gagal memproses file cadangan JSON: Format JSON rusak.');
          }}
        }};
        reader.readAsText(file);
      }},

      // Export CSV & JSON for Current Results
      exportCSV() {{
        if (!this.evaluationData) return;
        const letters = ['A', 'B', 'C', 'D'];
        let csvContent = `\uFEFF`;
        csvContent += `"LAPORAN HASIL SIMULASI CBT PERANGKAT DESA"\n`;
        csvContent += `"Nama Peserta","${{this.escapeCSV(this.candidateName)}}"\n`;
        csvContent += `"Wilayah","${{this.escapeCSV(this.region === 'tuban' ? 'Kabupaten Tuban' : 'Nasional')}}"\n`;
        csvContent += `"Tanggal","${{this.escapeCSV(new Date().toLocaleString('id-ID'))}}"\n\n`;
        csvContent += `"No","Kategori","Tingkat","Pertanyaan","Jawaban Peserta","Kunci Jawaban","Status","Pembahasan","Dasar Hukum"\n`;

        this.evaluationData.forEach(item => {{
          const userStr = item.isAnswered ? `${{letters[item.userAnswer]}}. ${{item.options[item.userAnswer]}}` : 'TIDAK DIJAWAB';
          const keyStr = `${{letters[item.keyAnswer]}}. ${{item.options[item.keyAnswer]}}`;
          csvContent += `"${{item.number}}","${{this.escapeCSV(item.category)}}","${{this.escapeCSV(item.difficulty)}}","${{this.escapeCSV(item.question)}}","${{this.escapeCSV(userStr)}}","${{this.escapeCSV(keyStr)}}","${{item.status.toUpperCase()}}","${{this.escapeCSV(item.explanation)}}","${{this.escapeCSV(item.source)}}"\n`;
        }});

        const blob = new Blob([csvContent], {{ type: 'text/csv;charset=utf-8;' }});
        this.downloadFile(blob, `Hasil_CBT_Perangkat_Desa_${{Date.now()}}.csv`);
      }},

      escapeCSV(text) {{
        return text ? String(text).replace(/"/g, '""') : '';
      }},

      exportJSON() {{
        if (!this.evaluationData) return;
        const obj = {{
          candidate: {{ name: this.candidateName, village: this.candidateVillage, region: this.region }},
          date: new Date().toISOString(),
          evaluations: this.evaluationData
        }};
        const blob = new Blob([JSON.stringify(obj, null, 2)], {{ type: 'application/json' }});
        this.downloadFile(blob, `Hasil_CBT_Perangkat_Desa_${{Date.now()}}.json`);
      }},

      downloadFile(blob, fileName) {{
        const link = document.createElement('a');
        link.href = URL.createObjectURL(blob);
        link.download = fileName;
        link.style.display = 'none';
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
      }},

      // Session save / resume
      saveSession() {{
        if (!this.isExamRunning || this.mode !== 'exam') return;
        safeSetStorage(this.STORAGE_KEY, {{
          mode: this.mode,
          region: this.region,
          candidateName: this.candidateName,
          candidateVillage: this.candidateVillage,
          currentIndex: this.currentIndex,
          userAnswers: this.userAnswers,
          flaggedQuestions: this.flaggedQuestions,
          visitedCount: this.visitedCount,
          examStartTime: this.examStartTime,
          inPriorityCycle: this.inPriorityCycle,
          questions: this.questions
        }});
      }},

      checkExistingSession() {{
        const saved = safeGetStorage(this.STORAGE_KEY, null);
        if (!saved) return;
        const elapsed = Date.now() - saved.examStartTime;
        if (elapsed < this.examDurationMs) {{
          const banner = document.getElementById('resumeBanner');
          if (banner) banner.style.display = 'flex';
        }} else {{
          safeSetStorage(this.STORAGE_KEY, null);
        }}
      }},

      resumeSession() {{
        const saved = safeGetStorage(this.STORAGE_KEY, null);
        if (!saved) return;

        this.mode = saved.mode || 'exam';
        this.region = saved.region || 'tuban';
        this.candidateName = saved.candidateName || 'Peserta';
        this.candidateVillage = saved.candidateVillage || '';
        this.currentIndex = saved.currentIndex || 0;
        this.userAnswers = saved.userAnswers || {{}};
        this.flaggedQuestions = saved.flaggedQuestions || {{}};
        this.visitedCount = saved.visitedCount || {{}};
        this.inPriorityCycle = !!saved.inPriorityCycle;
        this.examStartTime = saved.examStartTime;
        this.questionVisitStartTime = Date.now();
        this.questions = saved.questions || generateExam100Questions(MASTER_QUESTIONS, CATEGORIES_SPEC);
        this.isExamRunning = true;

        const banner = document.getElementById('resumeBanner');
        if (banner) banner.style.display = 'none';

        this.updateCandidateHeaderUI();
        this.renderQuestionPaletteGrid();
        this.renderCurrentQuestion();
        this.startTimerTickLoop();
        this.navigate('exam');
      }},

      clearSession() {{
        safeSetStorage(this.STORAGE_KEY, null);
        const banner = document.getElementById('resumeBanner');
        if (banner) banner.style.display = 'none';
      }},

      // Keyboard Shortcuts (A, B, C, D, Arrows, R, P, Esc)
      setupKeyboardShortcuts() {{
        window.addEventListener('keydown', (e) => {{
          if (e.key === 'Escape') {{
            this.closeModals();
            return;
          }}

          if (!this.isExamRunning || this.examSubmitted) return;
          if (e.target.tagName === 'INPUT' || e.target.tagName === 'SELECT' || e.target.tagName === 'TEXTAREA') return;

          const key = e.key.toUpperCase();
          if (key === 'A') this.selectOption(0);
          else if (key === 'B') this.selectOption(1);
          else if (key === 'C') this.selectOption(2);
          else if (key === 'D') this.selectOption(3);
          else if (e.key === 'ArrowLeft') this.prevQuestion();
          else if (e.key === 'ArrowRight') this.skipOrNextQuestion();
          else if (key === 'R' || key === 'F') this.toggleFlagCurrentQuestion();
        }});
      }}
    }};

    document.addEventListener('DOMContentLoaded', () => {{
      CBTApp.init();
    }});
  </script>
</body>
</html>
'''

    target_path = r"d:\FusionProject\Ujian\index.html"
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"[OK] index.html successfully generated with all 12 enhanced features ({len(html_content):,} bytes).")

if __name__ == "__main__":
    build_standalone_index()
