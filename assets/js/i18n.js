/**
 * Conmutador de idioma ES/EN/ZH/PT. Reemplaza el innerHTML de los elementos listados
 * en TRANSLATIONS y alterna cuál de los dos CV se enseña.
 *
 * OJO: hoy solo se carga en index.html. En las páginas generadas el selector se ve
 * pero no hace nada, porque este script vive tras el <footer> y _site.py no lo copia.
 */
(function() {
  var TRANSLATIONS = {
    en: {
      'brxe-roemkm': 'About_Me',
      'brxe-ldwmxs': 'Services',
      'brxe-hvforz': 'Real_Projects',
      'brxe-uklerk': 'Hire_Me',
      'brxe-wtyqnn': 'Full-stack web development specialist focused on scalable architectures and process automation. Integrating AI agents and solid technical infrastructure to optimize operations and performance.',
      'brxe-qfdlgb': 'About Me',
      'brxe-ohrdda': 'My professional journey started in digital marketing, where<br>I learned to understand user needs and the importance of data. However, my passion for solving complex problems led me to<br>dive deeper into the technology behind the strategies.',
      'brxe-fudjms': 'Today, as a Full-Stack Web &amp; Automation Expert, I combine strategic vision with advanced technical skills. I design robust architectures, implement complex automations and deploy AI agents to turn ideas into efficient, scalable systems.',
      'brxe-ezekjf': 'Services',
      'brxe-cdnwiz': ' Full digital strategy. From lead capture to conversion optimization and retention, ensuring maximum ROI. ',
      'brxe-zmdvfg': 'Web Development &amp; Architecture',
      'brxe-dlsums': 'WordPress + WooCommerce + Bricks Builder specialist. High-performance front-end and technical SEO. Building professional, accessible and scalable digital solutions from the ground up.',
      'brxe-lkgpwh': 'Automation &amp; Workflows',
      'brxe-ddpcii': 'Integrations using n8n, JSON-RPC and your CRM tool. Helping businesses optimize their operational logic through automation to maximize efficiency.',
      'brxe-pxcerv': 'Local Infrastructure',
      'brxe-vfrctw': 'Reducing operational costs through local infrastructure, dockerized environments, local AI, and Model Context Protocol (MCP) implementations.',
      'brxe-hmhnkk': 'SEO &amp; Performance',
      'brxe-qmgkfq': 'Technical SEO, Core Web Vitals optimization, and data analysis tools like SEMRush, GA4, Search Console and Screaming Frog.',
      'brxe-melzqw': 'Real_Projects // Success Stories',
      'brxe-ravryo': 'Cost optimization',
      'brxe-etglln': 'Internal Mail Marketing &amp; CRM Architecture.',
      'brxe-wdufrm': 'Development of a local CRM and mail marketing solution running on a local server. Integrated with Odoo and AWS Simple Email Service (SES) for secure high-volume email marketing, plus deployment of several internal services on the local server.',
      'brxe-kewgob': 'Immediate Impact',
      'brxe-pdkbbd': 'Efficiency Gained',
      'brxe-pwzhji': '3h/week saved',
      'brxe-afitrk': 'Automated Processes',
      'brxe-pxyake': 'Development of digital solutions to automate internal business processes, from lead management to communication and client outreach.',
      'brxe-qmuzqz': '<span style="font-size:3em; font-weight:600">100%</span><br><span class="label">Automated</span>',
      'brxe-kiilyy': '<span style="font-size:3em; font-weight:600">24/7</span><br><span class="label">Running</span>',
      'brxe-krcqzg': '<span style="font-size:3em; font-weight:600;color:#00e639">15h+</span><br><span class="label">Saved/Week</span>',
      'brxe-tigmdq': 'AI Chatbot in Personal Portfolio',
      'brxe-yrroqb': 'Try it now, ask it anything!',
      'brxe-cvzqdn': 'Website for a marketing agency',
      'brxe-mgtyet': 'Website for a sushi restaurant',
      'brxe-ainfry': 'Development',
      'brxe-cdjwpb': 'Automation &amp; AI',
      'brxe-yxvvkt': 'Infrastructure',
      'brxe-atbufs': ' © 2026 DHX_OS // Web development · AI automation · Infrastructure // v4.0 ',
      'brxe-blfnoa': 'Hermes AI Agent Deployment',
      'brxe-zstqih': '<span style="color:#00e639; font-weight:700">80€</span><span style="font-size:0.4em">/month saved</span>',
      'brxe-lobvgj': '<span style="color:#00f0ff"># Tech stack used</span><br>import <span style="color:#fed639">lm_studio</span><br>import <span style="color:#fed639">mcp_protocol</span><br>import <span style="color:#fed639">automate_reports</span>',
      'dhx-label-id': '&gt; Identifier=',
      'dhx-label-tx': '&gt; TX_Protocol=',
      'dhx-label-payload': '&gt; Payload='
    },
    zh: {
      'brxe-roemkm': '关于_我',
      'brxe-ldwmxs': '服务',
      'brxe-hvforz': '真实_项目',
      'brxe-uklerk': '雇用_我',
      'brxe-wtyqnn': '全栈网页开发专家,专注于可扩展架构和流程自动化。整合AI智能体与稳固的技术基础设施,以优化运营和性能。',
      'brxe-qfdlgb': '关于我',
      'brxe-ohrdda': '我的职业生涯始于数字营销领域,在那里<br>我学会了理解用户需求以及数据的重要性。然而,我对解决复杂问题的热情让我<br>深入研究策略背后的技术。',
      'brxe-fudjms': '如今,作为全栈网页与自动化专家,我将战略眼光与先进的技术能力相结合。我设计稳健的架构,实施复杂的自动化流程,并部署AI智能体,将想法转化为高效、可扩展的系统。',
      'brxe-ezekjf': '服务',
      'brxe-cdnwiz': ' 全方位数字战略。从潜在客户获取到转化优化与客户维系,确保最大化投资回报率(ROI)。 ',
      'brxe-zmdvfg': '网页开发与架构',
      'brxe-dlsums': 'WordPress + WooCommerce + Bricks Builder专家。高性能前端与技术SEO。从根基开始打造专业、无障碍且可扩展的数字化解决方案。',
      'brxe-lkgpwh': '自动化与工作流',
      'brxe-ddpcii': '使用n8n、JSON-RPC以及你的CRM工具进行集成。帮助企业通过自动化优化业务逻辑,最大化运营效率。',
      'brxe-pxcerv': '本地基础设施',
      'brxe-vfrctw': '通过本地基础设施、Docker化环境、本地人工智能以及模型上下文协议(MCP)的实施,降低运营成本。',
      'brxe-hmhnkk': 'SEO与性能优化',
      'brxe-qmgkfq': '技术SEO、Core Web Vitals优化,以及使用SEMRush、GA4、Search Console和Screaming Frog等工具进行数据分析。',
      'brxe-melzqw': '真实_项目 // 成功案例',
      'brxe-ravryo': '成本优化',
      'brxe-etglln': '内部邮件营销与CRM架构。',
      'brxe-wdufrm': '在本地服务器上开发本地CRM与邮件营销解决方案。集成Odoo与AWS Simple Email Service(SES),实现安全的大批量邮件营销,并在本地服务器内部署多项内部服务。',
      'brxe-kewgob': '即时影响',
      'brxe-pdkbbd': '获得的效率',
      'brxe-pwzhji': '每周节省3小时',
      'brxe-afitrk': '自动化流程',
      'brxe-pxyake': '开发数字化解决方案,满足企业内部流程自动化需求,从潜在客户管理到与客户的沟通联系。',
      'brxe-qmuzqz': '<span style="font-size:3em; font-weight:600">100%</span><br><span class="label">自动化</span>',
      'brxe-kiilyy': '<span style="font-size:3em; font-weight:600">24/7</span><br><span class="label">运行中</span>',
      'brxe-krcqzg': '<span style="font-size:3em; font-weight:600;color:#00e639">15h+</span><br><span class="label">每周节省</span>',
      'brxe-tigmdq': '个人作品集中的AI聊天机器人',
      'brxe-yrroqb': '现在就试试,问它任何问题!',
      'brxe-cvzqdn': '营销机构网站',
      'brxe-mgtyet': '寿司自助餐厅网站',
      'brxe-ainfry': '开发',
      'brxe-cdjwpb': '自动化与AI',
      'brxe-yxvvkt': '基础设施',
      'brxe-atbufs': ' © 2026 DHX_OS // 网页开发 · AI自动化 · 基础设施 // v4.0 ',
      'brxe-blfnoa': 'Hermes AI智能体部署',
      'brxe-zstqih': '<span style="color:#00e639; font-weight:700">80€</span><span style="font-size:0.4em">/月节省</span>',
      'brxe-lobvgj': '<span style="color:#00f0ff"># 使用的技术栈</span><br>import <span style="color:#fed639">lm_studio</span><br>import <span style="color:#fed639">mcp_protocol</span><br>import <span style="color:#fed639">automate_reports</span>',
      'dhx-label-id': '&gt; 标识符=',
      'dhx-label-tx': '&gt; 发送协议=',
      'dhx-label-payload': '&gt; Payload='
    },
    pt: {
      'brxe-roemkm': 'Sobre_Mim',
      'brxe-ldwmxs': 'Serviços',
      'brxe-hvforz': 'Projetos_Reais',
      'brxe-uklerk': 'Contrate_Me',
      'brxe-wtyqnn': 'Especialista em desenvolvimento web full-stack, focado em arquiteturas escaláveis e automação de processos. Integrando agentes de IA e infraestrutura técnica sólida para otimizar operações e desempenho.',
      'brxe-qfdlgb': 'Sobre Mim',
      'brxe-ohrdda': 'A minha evolução profissional começou no mundo do marketing digital, onde<br>aprendi a entender as necessidades do utilizador e a importância dos dados. No entanto, a minha paixão por resolver problemas complexos levou-me a<br>aprofundar-me na tecnologia por trás das estratégias.',
      'brxe-fudjms': 'Hoje, como Full-Stack Web &amp; Automation Expert, combino a minha visão estratégica com competências técnicas avançadas. Desenho arquiteturas robustas, implemento automações complexas e implanto agentes de IA para transformar ideias em sistemas eficientes e escaláveis.',
      'brxe-ezekjf': 'Serviços',
      'brxe-cdnwiz': ' Estratégia digital integral. Da captura de leads à otimização da conversão e fidelização, garantindo o máximo ROI. ',
      'brxe-zmdvfg': 'Desenvolvimento Web e Arquitetura Web',
      'brxe-dlsums': 'Especialista em WordPress + WooCommerce + Bricks Builder. Front-end de alta performance e SEO técnico. A criar soluções digitais profissionais, acessíveis e escaláveis desde a base.',
      'brxe-lkgpwh': 'Automações e Workflows',
      'brxe-ddpcii': 'Integrações usando n8n, JSON-RPC e a tua ferramenta de CRM. A ajudar empresas a otimizar a lógica empresarial através de automações para maximizar a eficiência operacional.',
      'brxe-pxcerv': 'Infraestrutura Local',
      'brxe-vfrctw': 'Redução de custos operacionais através de infraestrutura local, ambientes dockerizados, Inteligência Artificial local e implementações do Model Context Protocol (MCP).',
      'brxe-hmhnkk': 'SEO e Desempenho',
      'brxe-qmgkfq': 'SEO técnico, otimização de Core Web Vitals e uso de ferramentas de análise de dados como SEMRush, GA4, Search Console e Screaming Frog.',
      'brxe-melzqw': 'Projetos_Reais // Casos de Sucesso',
      'brxe-ravryo': 'Otimização de custos',
      'brxe-etglln': 'Arquitetura de Mail Marketing e CRM interno.',
      'brxe-wdufrm': 'Desenvolvimento de uma solução local de CRM e Mail Marketing, num servidor local. Integrado com Odoo e AWS Simple Email Service (SES) para o alto volume de mail marketing de forma segura, além da instalação de diversos serviços dentro do servidor local para uso interno.',
      'brxe-kewgob': 'Impacto Imediato',
      'brxe-pdkbbd': 'Eficiência Obtida',
      'brxe-pwzhji': '3h/semana poupadas',
      'brxe-afitrk': 'Processos Automatizados',
      'brxe-pxyake': 'Desenvolvimento de soluções digitais para as necessidades de automatizar processos internos da empresa, desde a gestão de leads até à comunicação e contacto com os clientes.',
      'brxe-qmuzqz': '<span style="font-size:3em; font-weight:600">100%</span><br><span class="label">Automatizado</span>',
      'brxe-kiilyy': '<span style="font-size:3em; font-weight:600">24/7</span><br><span class="label">Em Operação</span>',
      'brxe-krcqzg': '<span style="font-size:3em; font-weight:600;color:#00e639">15h+</span><br><span class="label">Poupadas/Semana</span>',
      'brxe-tigmdq': 'Chatbot de IA no Portfólio Pessoal',
      'brxe-yrroqb': 'Experimenta já, pergunta o que quiseres!',
      'brxe-cvzqdn': 'Website para agência de marketing',
      'brxe-mgtyet': 'Website para restaurante de sushi',
      'brxe-ainfry': 'Desenvolvimento',
      'brxe-cdjwpb': 'Automação e IA',
      'brxe-yxvvkt': 'Infraestrutura',
      'brxe-atbufs': ' © 2026 DHX_OS // Desenvolvimento web · Automação com IA · Infraestrutura // v4.0 ',
      'brxe-blfnoa': 'Implementação do Agente de IA Hermes',
      'brxe-zstqih': '<span style="color:#00e639; font-weight:700">80€</span><span style="font-size:0.4em">/mês poupados</span>',
      'brxe-lobvgj': '<span style="color:#00f0ff"># Stack técnico utilizado</span><br>import <span style="color:#fed639">lm_studio</span><br>import <span style="color:#fed639">mcp_protocol</span><br>import <span style="color:#fed639">automate_reports</span>',
      'dhx-label-id': '&gt; Identificador=',
      'dhx-label-tx': '&gt; Protocolo_TX=',
      'dhx-label-payload': '&gt; Payload='
    }
  };
  var PLACEHOLDERS = {
    en: { 'dhx-nombre': 'Your name', 'dhx-email': 'email@domain.com', 'dhx-mensaje': 'Describe your project or inquiry...' },
    zh: { 'dhx-nombre': '你的姓名', 'dhx-email': 'email@domain.com', 'dhx-mensaje': '描述你的项目或咨询...' },
    pt: { 'dhx-nombre': 'O teu nome', 'dhx-email': 'email@dominio.com', 'dhx-mensaje': 'Descreve o projeto ou consulta...' }
  };
  var MESSAGES = {
    es: { required: '> Error: campos obligatorios vacios.', sent: '> Transmision completada. Respondere pronto.', sendError: '> Error en la transmision. Intentalo de nuevo.', connError: '> Error de conexion. Comprueba tu red.' },
    en: { required: '> Error: required fields are empty.', sent: '> Transmission complete. I will get back to you soon.', sendError: '> Transmission error. Please try again.', connError: '> Connection error. Check your network.' },
    zh: { required: '> 错误:必填字段为空。', sent: '> 发送成功,我会尽快回复。', sendError: '> 发送错误,请重试。', connError: '> 连接错误,请检查网络。' },
    pt: { required: '> Erro: campos obrigatórios vazios.', sent: '> Transmissão concluída. Responderei em breve.', sendError: '> Erro na transmissão. Tenta novamente.', connError: '> Erro de conexão. Verifica a tua rede.' }
  };
  var ORIGINAL = {};
  var PLACEHOLDERS_ES = {};
  var LANG_KEY = 'dhx_lang';

  function applyLang(lang) {
    var dict = TRANSLATIONS[lang];
    var ids = TRANSLATIONS.en;
    for (var id in ids) {
      if (!Object.prototype.hasOwnProperty.call(ids, id)) { continue; }
      var el = document.getElementById(id);
      if (!el) { continue; }
      if (!(id in ORIGINAL)) { ORIGINAL[id] = el.innerHTML; }
      el.innerHTML = (lang === 'es' || !dict) ? ORIGINAL[id] : dict[id];
    }
    var ph = PLACEHOLDERS[lang];
    for (var pid in PLACEHOLDERS.en) {
      if (!Object.prototype.hasOwnProperty.call(PLACEHOLDERS.en, pid)) { continue; }
      var input = document.getElementById(pid);
      if (!input) { continue; }
      if (!(pid in PLACEHOLDERS_ES)) { PLACEHOLDERS_ES[pid] = input.placeholder; }
      input.placeholder = (lang === 'es' || !ph) ? PLACEHOLDERS_ES[pid] : ph[pid];
    }

    var linkEs = document.querySelector('a[href*="cv-david-huang-xie-es.pdf"]');
    var linkEn = document.querySelector('a[href*="cv-david-huang-xie-en.pdf"]');
    if (linkEs) { linkEs.style.display = (lang === 'es') ? '' : 'none'; }
    if (linkEn) { linkEn.style.display = (lang === 'es') ? 'none' : ''; }

    document.documentElement.lang = lang;
    window.DHX_LANG = lang;

    var opts = document.querySelectorAll('.dhx-lang-opt');
    for (var i = 0; i < opts.length; i++) {
      var active = opts[i].getAttribute('data-lang') === lang;
      opts[i].style.color = active ? '#00f0ff' : '#849495';
      opts[i].style.fontWeight = active ? '700' : '400';
    }

    try { localStorage.setItem(LANG_KEY, lang); } catch (e) {}
  }

  document.addEventListener('DOMContentLoaded', function() {
    var saved = 'es';
    try { saved = localStorage.getItem(LANG_KEY) || 'es'; } catch (e) {}
    applyLang(saved);

    var opts = document.querySelectorAll('.dhx-lang-opt');
    for (var i = 0; i < opts.length; i++) {
      opts[i].addEventListener('click', function() { applyLang(this.getAttribute('data-lang')); });
    }
  });

  window.DHX_MESSAGES = MESSAGES;
})();
