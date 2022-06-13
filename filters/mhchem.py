__all__ = ['mhchem']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['assertNever', '_mhchemCreateTransitions', '_mhchemParser', '_mhchemTexify', 'mhchemParser'])
@Js
def PyJsHoisted__mhchemCreateTransitions_(o, this, arguments, var=var):
    var = Scope({'o':o, 'this':this, 'arguments':arguments}, var)
    var.registers(['p', 'transitions', 'o', 'stateArray', 'patternArray', 'state', 'j', 'pattern', 't', 'k', 'i'])
    pass
    var.put('transitions', Js({}))
    for PyJsTemp in var.get('o'):
        var.put('pattern', PyJsTemp)
        for PyJsTemp in var.get('o').get(var.get('pattern')):
            var.put('state', PyJsTemp)
            var.put('stateArray', var.get('state').callprop('split', Js('|')))
            var.get('o').get(var.get('pattern')).get(var.get('state')).put('stateArray', var.get('stateArray'))
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get('stateArray').get('length')):
                try:
                    var.get('transitions').put(var.get('stateArray').get(var.get('i')), Js([]))
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    for PyJsTemp in var.get('o'):
        var.put('pattern', PyJsTemp)
        for PyJsTemp in var.get('o').get(var.get('pattern')):
            var.put('state', PyJsTemp)
            var.put('stateArray', (var.get('o').get(var.get('pattern')).get(var.get('state')).get('stateArray') or Js([])))
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get('stateArray').get('length')):
                try:
                    var.put('p', var.get('o').get(var.get('pattern')).get(var.get('state')))
                    var.get('p').put('action_', Js([]).callprop('concat', var.get('p').get('action_')))
                    #for JS loop
                    var.put('k', Js(0.0))
                    while (var.get('k')<var.get('p').get('action_').get('length')):
                        try:
                            if PyJsStrictEq(var.get('p').get('action_').get(var.get('k')).typeof(),Js('string')):
                                var.get('p').get('action_').put(var.get('k'), Js({'type_':var.get('p').get('action_').get(var.get('k'))}))
                        finally:
                                (var.put('k',Js(var.get('k').to_number())+Js(1))-Js(1))
                    var.put('patternArray', var.get('pattern').callprop('split', Js('|')))
                    #for JS loop
                    var.put('j', Js(0.0))
                    while (var.get('j')<var.get('patternArray').get('length')):
                        try:
                            if PyJsStrictEq(var.get('stateArray').get(var.get('i')),Js('*')):
                                var.put('t', PyJsComma(Js(0.0), Js(None)))
                                for PyJsTemp in var.get('transitions'):
                                    var.put('t', PyJsTemp)
                                    var.get('transitions').get(var.get('t')).callprop('push', Js({'pattern':var.get('patternArray').get(var.get('j')),'task':var.get('p')}))
                            else:
                                var.get('transitions').get(var.get('stateArray').get(var.get('i'))).callprop('push', Js({'pattern':var.get('patternArray').get(var.get('j')),'task':var.get('p')}))
                        finally:
                                (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    return var.get('transitions')
PyJsHoisted__mhchemCreateTransitions_.func_name = '_mhchemCreateTransitions'
var.put('_mhchemCreateTransitions', PyJsHoisted__mhchemCreateTransitions_)
@Js
def PyJsHoisted_assertNever_(a, this, arguments, var=var):
    var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
    var.registers(['a'])
    pass
PyJsHoisted_assertNever_.func_name = 'assertNever'
var.put('assertNever', PyJsHoisted_assertNever_)
Js('use strict')
var.put('exports', Js({}))
var.get('Object').callprop('defineProperty', var.get('exports'), Js('__esModule'), Js({'value':Js(True)}))
var.get('exports').put('mhchemParser', PyJsComma(Js(0.0), Js(None)))
@Js
def PyJs_anonymous_0_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['mhchemParser'])
    @Js
    def PyJsHoisted_mhchemParser_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        pass
    PyJsHoisted_mhchemParser_.func_name = 'mhchemParser'
    var.put('mhchemParser', PyJsHoisted_mhchemParser_)
    pass
    @Js
    def PyJs_anonymous_1_(input, type, this, arguments, var=var):
        var = Scope({'input':input, 'type':type, 'this':this, 'arguments':arguments}, var)
        var.registers(['type', 'input'])
        return var.get('_mhchemTexify').callprop('go', var.get('_mhchemParser').callprop('go', var.get('input'), var.get('type')), PyJsStrictNeq(var.get('type'),Js('tex')))
    PyJs_anonymous_1_._set_name('anonymous')
    var.get('mhchemParser').put('toTex', PyJs_anonymous_1_)
    return var.get('mhchemParser')
PyJs_anonymous_0_._set_name('anonymous')
var.put('mhchemParser', PyJs_anonymous_0_())
var.get('exports').put('mhchemParser', var.get('mhchemParser'))
pass
@Js
def PyJs_anonymous_2_(input, stateMachine, this, arguments, var=var):
    var = Scope({'input':input, 'stateMachine':stateMachine, 'this':this, 'arguments':arguments}, var)
    var.registers(['stateMachine', 'buffer', 'machine', 'o', 'matches', 'i', 'input', 'output', 'task', 'iA', 'lastInput', 'state', 't', 'watchdog'])
    if var.get('input').neg():
        return Js([])
    if PyJsStrictEq(var.get('stateMachine'),var.get('undefined')):
        var.put('stateMachine', Js('ce'))
    var.put('state', Js('0'))
    var.put('buffer', Js({}))
    var.get('buffer').put('parenthesisLevel', Js(0.0))
    var.put('input', var.get('input').callprop('replace', JsRegExp('/\\n/g'), Js(' ')))
    var.put('input', var.get('input').callprop('replace', JsRegExp('/[\\u2212\\u2013\\u2014\\u2010]/g'), Js('-')))
    var.put('input', var.get('input').callprop('replace', JsRegExp('/[\\u2026]/g'), Js('...')))
    pass
    var.put('watchdog', Js(10.0))
    var.put('output', Js([]))
    while Js(True):
        if PyJsStrictNeq(var.get('lastInput'),var.get('input')):
            var.put('watchdog', Js(10.0))
            var.put('lastInput', var.get('input'))
        else:
            (var.put('watchdog',Js(var.get('watchdog').to_number())-Js(1))+Js(1))
        var.put('machine', var.get('_mhchemParser').get('stateMachines').get(var.get('stateMachine')))
        var.put('t', (var.get('machine').get('transitions').get(var.get('state')) or var.get('machine').get('transitions').get('*')))
        class JS_CONTINUE_LABEL_697465726174655472616e736974696f6e73(Exception): pass
        class JS_BREAK_LABEL_697465726174655472616e736974696f6e73(Exception): pass
        try:
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get('t').get('length')):
                try:
                    try:
                        var.put('matches', var.get('_mhchemParser').get('patterns').callprop('match_', var.get('t').get(var.get('i')).get('pattern'), var.get('input')))
                        if var.get('matches'):
                            var.put('task', var.get('t').get(var.get('i')).get('task'))
                            #for JS loop
                            var.put('iA', Js(0.0))
                            while (var.get('iA')<var.get('task').get('action_').get('length')):
                                try:
                                    var.put('o', PyJsComma(Js(0.0), Js(None)))
                                    if var.get('machine').get('actions').get(var.get('task').get('action_').get(var.get('iA')).get('type_')):
                                        var.put('o', var.get('machine').get('actions').callprop(var.get('task').get('action_').get(var.get('iA')).get('type_'), var.get('buffer'), var.get('matches').get('match_'), var.get('task').get('action_').get(var.get('iA')).get('option')))
                                    else:
                                        if var.get('_mhchemParser').get('actions').get(var.get('task').get('action_').get(var.get('iA')).get('type_')):
                                            var.put('o', var.get('_mhchemParser').get('actions').callprop(var.get('task').get('action_').get(var.get('iA')).get('type_'), var.get('buffer'), var.get('matches').get('match_'), var.get('task').get('action_').get(var.get('iA')).get('option')))
                                        else:
                                            PyJsTempException = JsToPyException(Js([Js('MhchemBugA'), ((Js('mhchem bug A. Please report. (')+var.get('task').get('action_').get(var.get('iA')).get('type_'))+Js(')'))]))
                                            raise PyJsTempException
                                    var.get('_mhchemParser').callprop('concatArray', var.get('output'), var.get('o'))
                                finally:
                                        (var.put('iA',Js(var.get('iA').to_number())+Js(1))-Js(1))
                            var.put('state', (var.get('task').get('nextState') or var.get('state')))
                            if (var.get('input').get('length')>Js(0.0)):
                                if var.get('task').get('revisit').neg():
                                    var.put('input', var.get('matches').get('remainder'))
                                if var.get('task').get('toContinue').neg():
                                    raise JS_BREAK_LABEL_697465726174655472616e736974696f6e73("Breaked")
                            else:
                                return var.get('output')
                    finally:
                            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                except JS_CONTINUE_LABEL_697465726174655472616e736974696f6e73:
                    pass
        except JS_BREAK_LABEL_697465726174655472616e736974696f6e73:
            pass
        if (var.get('watchdog')<=Js(0.0)):
            PyJsTempException = JsToPyException(Js([Js('MhchemBugU'), Js('mhchem bug U. Please report.')]))
            raise PyJsTempException
PyJs_anonymous_2_._set_name('anonymous')
@Js
def PyJs_anonymous_3_(a, b, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'this':this, 'arguments':arguments}, var)
    var.registers(['iB', 'b', 'a'])
    if var.get('b'):
        if var.get('Array').callprop('isArray', var.get('b')):
            #for JS loop
            var.put('iB', Js(0.0))
            while (var.get('iB')<var.get('b').get('length')):
                try:
                    var.get('a').callprop('push', var.get('b').get(var.get('iB')))
                finally:
                        (var.put('iB',Js(var.get('iB').to_number())+Js(1))-Js(1))
        else:
            var.get('a').callprop('push', var.get('b'))
PyJs_anonymous_3_._set_name('anonymous')
@Js
def PyJs_anonymous_4_(input, this, arguments, var=var):
    var = Scope({'input':input, 'this':this, 'arguments':arguments}, var)
    var.registers(['match', 'input'])
    var.put('match', var.get('input').callprop('match', JsRegExp('/^(\\+\\-|\\+\\/\\-|\\+|\\-|\\\\pm\\s?)?([0-9]+(?:[,.][0-9]+)?|[0-9]*(?:\\.[0-9]+))?(\\((?:[0-9]+(?:[,.][0-9]+)?|[0-9]*(?:\\.[0-9]+))\\))?(?:(?:([eE])|\\s*(\\*|x|\\\\times|\\u00D7)\\s*10\\^)([+\\-]?[0-9]+|\\{[+\\-]?[0-9]+\\}))?/')))
    if (var.get('match') and var.get('match').get('0')):
        return Js({'match_':var.get('match').callprop('slice', Js(1.0)),'remainder':var.get('input').callprop('substr', var.get('match').get('0').get('length'))})
    return var.get(u"null")
PyJs_anonymous_4_._set_name('anonymous')
@Js
def PyJs_anonymous_5_(input, this, arguments, var=var):
    var = Scope({'input':input, 'this':this, 'arguments':arguments}, var)
    var.registers(['a', 'match', 'input'])
    var.put('a', var.get('_mhchemParser').get('patterns').callprop('findObserveGroups', var.get('input'), Js(''), JsRegExp('/^\\([a-z]{1,3}(?=[\\),])/'), Js(')'), Js('')))
    if (var.get('a') and var.get('a').get('remainder').callprop('match', JsRegExp('/^($|[\\s,;\\)\\]\\}])/'))):
        return var.get('a')
    var.put('match', var.get('input').callprop('match', JsRegExp('/^(?:\\((?:\\\\ca\\s?)?\\$[amothc]\\$\\))/')))
    if var.get('match'):
        return Js({'match_':var.get('match').get('0'),'remainder':var.get('input').callprop('substr', var.get('match').get('0').get('length'))})
    return var.get(u"null")
PyJs_anonymous_5_._set_name('anonymous')
@Js
def PyJs_anonymous_6_(input, this, arguments, var=var):
    var = Scope({'input':input, 'this':this, 'arguments':arguments}, var)
    var.registers(['input'])
    return var.get('_mhchemParser').get('patterns').callprop('findObserveGroups', var.get('input'), Js('^{'), Js(''), Js(''), Js('}'))
PyJs_anonymous_6_._set_name('anonymous')
@Js
def PyJs_anonymous_7_(input, this, arguments, var=var):
    var = Scope({'input':input, 'this':this, 'arguments':arguments}, var)
    var.registers(['input'])
    return var.get('_mhchemParser').get('patterns').callprop('findObserveGroups', var.get('input'), Js('^'), Js('$'), Js('$'), Js(''))
PyJs_anonymous_7_._set_name('anonymous')
@Js
def PyJs_anonymous_8_(input, this, arguments, var=var):
    var = Scope({'input':input, 'this':this, 'arguments':arguments}, var)
    var.registers(['input'])
    return var.get('_mhchemParser').get('patterns').callprop('findObserveGroups', var.get('input'), Js('^'), JsRegExp('/^\\\\[a-zA-Z]+\\{/'), Js('}'), Js(''), Js(''), Js('{'), Js('}'), Js(''), Js(True))
PyJs_anonymous_8_._set_name('anonymous')
@Js
def PyJs_anonymous_9_(input, this, arguments, var=var):
    var = Scope({'input':input, 'this':this, 'arguments':arguments}, var)
    var.registers(['input'])
    return var.get('_mhchemParser').get('patterns').callprop('findObserveGroups', var.get('input'), Js('^'), JsRegExp('/^\\\\[a-zA-Z]+\\{/'), Js('}'), Js(''))
PyJs_anonymous_9_._set_name('anonymous')
@Js
def PyJs_anonymous_10_(input, this, arguments, var=var):
    var = Scope({'input':input, 'this':this, 'arguments':arguments}, var)
    var.registers(['input'])
    return var.get('_mhchemParser').get('patterns').callprop('findObserveGroups', var.get('input'), Js('_{'), Js(''), Js(''), Js('}'))
PyJs_anonymous_10_._set_name('anonymous')
@Js
def PyJs_anonymous_11_(input, this, arguments, var=var):
    var = Scope({'input':input, 'this':this, 'arguments':arguments}, var)
    var.registers(['input'])
    return var.get('_mhchemParser').get('patterns').callprop('findObserveGroups', var.get('input'), Js('_'), Js('$'), Js('$'), Js(''))
PyJs_anonymous_11_._set_name('anonymous')
@Js
def PyJs_anonymous_12_(input, this, arguments, var=var):
    var = Scope({'input':input, 'this':this, 'arguments':arguments}, var)
    var.registers(['input'])
    return var.get('_mhchemParser').get('patterns').callprop('findObserveGroups', var.get('input'), Js('_'), JsRegExp('/^\\\\[a-zA-Z]+\\{/'), Js('}'), Js(''), Js(''), Js('{'), Js('}'), Js(''), Js(True))
PyJs_anonymous_12_._set_name('anonymous')
@Js
def PyJs_anonymous_13_(input, this, arguments, var=var):
    var = Scope({'input':input, 'this':this, 'arguments':arguments}, var)
    var.registers(['input'])
    return var.get('_mhchemParser').get('patterns').callprop('findObserveGroups', var.get('input'), Js('_'), JsRegExp('/^\\\\[a-zA-Z]+\\{/'), Js('}'), Js(''))
PyJs_anonymous_13_._set_name('anonymous')
@Js
def PyJs_anonymous_14_(input, this, arguments, var=var):
    var = Scope({'input':input, 'this':this, 'arguments':arguments}, var)
    var.registers(['input'])
    return var.get('_mhchemParser').get('patterns').callprop('findObserveGroups', var.get('input'), Js(''), Js('{'), Js('}'), Js(''))
PyJs_anonymous_14_._set_name('anonymous')
@Js
def PyJs_anonymous_15_(input, this, arguments, var=var):
    var = Scope({'input':input, 'this':this, 'arguments':arguments}, var)
    var.registers(['input'])
    return var.get('_mhchemParser').get('patterns').callprop('findObserveGroups', var.get('input'), Js('{'), Js(''), Js(''), Js('}'))
PyJs_anonymous_15_._set_name('anonymous')
@Js
def PyJs_anonymous_16_(input, this, arguments, var=var):
    var = Scope({'input':input, 'this':this, 'arguments':arguments}, var)
    var.registers(['input'])
    return var.get('_mhchemParser').get('patterns').callprop('findObserveGroups', var.get('input'), Js(''), Js('$'), Js('$'), Js(''))
PyJs_anonymous_16_._set_name('anonymous')
@Js
def PyJs_anonymous_17_(input, this, arguments, var=var):
    var = Scope({'input':input, 'this':this, 'arguments':arguments}, var)
    var.registers(['input'])
    return (var.get('_mhchemParser').get('patterns').callprop('findObserveGroups', var.get('input'), Js('${'), Js(''), Js(''), Js('}$')) or var.get('_mhchemParser').get('patterns').callprop('findObserveGroups', var.get('input'), Js('$'), Js(''), Js(''), Js('$')))
PyJs_anonymous_17_._set_name('anonymous')
@Js
def PyJs_anonymous_18_(input, this, arguments, var=var):
    var = Scope({'input':input, 'this':this, 'arguments':arguments}, var)
    var.registers(['input'])
    return var.get('_mhchemParser').get('patterns').callprop('findObserveGroups', var.get('input'), Js('\\bond{'), Js(''), Js(''), Js('}'))
PyJs_anonymous_18_._set_name('anonymous')
@Js
def PyJs_anonymous_19_(input, this, arguments, var=var):
    var = Scope({'input':input, 'this':this, 'arguments':arguments}, var)
    var.registers(['input'])
    return var.get('_mhchemParser').get('patterns').callprop('findObserveGroups', var.get('input'), Js('['), Js(''), Js(''), Js(']'))
PyJs_anonymous_19_._set_name('anonymous')
@Js
def PyJs_anonymous_20_(input, this, arguments, var=var):
    var = Scope({'input':input, 'this':this, 'arguments':arguments}, var)
    var.registers(['input'])
    return var.get('_mhchemParser').get('patterns').callprop('findObserveGroups', var.get('input'), Js(''), JsRegExp('/^\\\\[a-zA-Z]+\\{/'), Js('}'), Js(''), Js(''), Js('{'), Js('}'), Js(''), Js(True))
PyJs_anonymous_20_._set_name('anonymous')
@Js
def PyJs_anonymous_21_(input, this, arguments, var=var):
    var = Scope({'input':input, 'this':this, 'arguments':arguments}, var)
    var.registers(['input'])
    return var.get('_mhchemParser').get('patterns').callprop('findObserveGroups', var.get('input'), Js(''), JsRegExp('/^\\\\[a-zA-Z]+\\{/'), Js('}'), Js(''))
PyJs_anonymous_21_._set_name('anonymous')
@Js
def PyJs_anonymous_22_(input, this, arguments, var=var):
    var = Scope({'input':input, 'this':this, 'arguments':arguments}, var)
    var.registers(['input'])
    return var.get('_mhchemParser').get('patterns').callprop('findObserveGroups', var.get('input'), Js('\\frac{'), Js(''), Js(''), Js('}'), Js('{'), Js(''), Js(''), Js('}'))
PyJs_anonymous_22_._set_name('anonymous')
@Js
def PyJs_anonymous_23_(input, this, arguments, var=var):
    var = Scope({'input':input, 'this':this, 'arguments':arguments}, var)
    var.registers(['input'])
    return var.get('_mhchemParser').get('patterns').callprop('findObserveGroups', var.get('input'), Js('\\overset{'), Js(''), Js(''), Js('}'), Js('{'), Js(''), Js(''), Js('}'))
PyJs_anonymous_23_._set_name('anonymous')
@Js
def PyJs_anonymous_24_(input, this, arguments, var=var):
    var = Scope({'input':input, 'this':this, 'arguments':arguments}, var)
    var.registers(['input'])
    return var.get('_mhchemParser').get('patterns').callprop('findObserveGroups', var.get('input'), Js('\\underset{'), Js(''), Js(''), Js('}'), Js('{'), Js(''), Js(''), Js('}'))
PyJs_anonymous_24_._set_name('anonymous')
@Js
def PyJs_anonymous_25_(input, this, arguments, var=var):
    var = Scope({'input':input, 'this':this, 'arguments':arguments}, var)
    var.registers(['input'])
    return var.get('_mhchemParser').get('patterns').callprop('findObserveGroups', var.get('input'), Js('\\underbrace{'), Js(''), Js(''), Js('}_'), Js('{'), Js(''), Js(''), Js('}'))
PyJs_anonymous_25_._set_name('anonymous')
@Js
def PyJs_anonymous_26_(input, this, arguments, var=var):
    var = Scope({'input':input, 'this':this, 'arguments':arguments}, var)
    var.registers(['input'])
    return var.get('_mhchemParser').get('patterns').callprop('findObserveGroups', var.get('input'), Js('\\color{'), Js(''), Js(''), Js('}'))
PyJs_anonymous_26_._set_name('anonymous')
@Js
def PyJs_anonymous_27_(input, this, arguments, var=var):
    var = Scope({'input':input, 'this':this, 'arguments':arguments}, var)
    var.registers(['input'])
    return (var.get('_mhchemParser').get('patterns').callprop('findObserveGroups', var.get('input'), Js('\\color{'), Js(''), Js(''), Js('}'), Js('{'), Js(''), Js(''), Js('}')) or var.get('_mhchemParser').get('patterns').callprop('findObserveGroups', var.get('input'), Js('\\color'), Js('\\'), Js(''), JsRegExp('/^(?=\\{)/'), Js('{'), Js(''), Js(''), Js('}')))
PyJs_anonymous_27_._set_name('anonymous')
@Js
def PyJs_anonymous_28_(input, this, arguments, var=var):
    var = Scope({'input':input, 'this':this, 'arguments':arguments}, var)
    var.registers(['input'])
    return var.get('_mhchemParser').get('patterns').callprop('findObserveGroups', var.get('input'), Js('\\ce{'), Js(''), Js(''), Js('}'))
PyJs_anonymous_28_._set_name('anonymous')
@Js
def PyJs_anonymous_29_(input, this, arguments, var=var):
    var = Scope({'input':input, 'this':this, 'arguments':arguments}, var)
    var.registers(['input'])
    return var.get('_mhchemParser').get('patterns').callprop('findObserveGroups', var.get('input'), Js('\\pu{'), Js(''), Js(''), Js('}'))
PyJs_anonymous_29_._set_name('anonymous')
@Js
def PyJs_anonymous_30_(input, this, arguments, var=var):
    var = Scope({'input':input, 'this':this, 'arguments':arguments}, var)
    var.registers(['a', 'match', 'input'])
    pass
    var.put('match', var.get('input').callprop('match', JsRegExp('/^(?:(?:(?:\\([+\\-]?[0-9]+\\/[0-9]+\\)|[+\\-]?(?:[0-9]+|\\$[a-z]\\$|[a-z])\\/[0-9]+|[+\\-]?[0-9]+[.,][0-9]+|[+\\-]?\\.[0-9]+|[+\\-]?[0-9]+)(?:[a-z](?=\\s*[A-Z]))?)|[+\\-]?[a-z](?=\\s*[A-Z])|\\+(?!\\s))/')))
    if var.get('match'):
        return Js({'match_':var.get('match').get('0'),'remainder':var.get('input').callprop('substr', var.get('match').get('0').get('length'))})
    var.put('a', var.get('_mhchemParser').get('patterns').callprop('findObserveGroups', var.get('input'), Js(''), Js('$'), Js('$'), Js('')))
    if var.get('a'):
        var.put('match', var.get('a').get('match_').callprop('match', JsRegExp('/^\\$(?:\\(?[+\\-]?(?:[0-9]*[a-z]?[+\\-])?[0-9]*[a-z](?:[+\\-][0-9]*[a-z]?)?\\)?|\\+|-)\\$$/')))
        if var.get('match'):
            return Js({'match_':var.get('match').get('0'),'remainder':var.get('input').callprop('substr', var.get('match').get('0').get('length'))})
    return var.get(u"null")
PyJs_anonymous_30_._set_name('anonymous')
@Js
def PyJs_anonymous_31_(input, this, arguments, var=var):
    var = Scope({'input':input, 'this':this, 'arguments':arguments}, var)
    var.registers(['input'])
    return var.get(u"this").callprop('amount', var.get('input'))
PyJs_anonymous_31_._set_name('anonymous')
@Js
def PyJs_anonymous_32_(input, this, arguments, var=var):
    var = Scope({'input':input, 'this':this, 'arguments':arguments}, var)
    var.registers(['match', 'input'])
    if var.get('input').callprop('match', JsRegExp('/^\\([a-z]+\\)$/')):
        return var.get(u"null")
    var.put('match', var.get('input').callprop('match', JsRegExp('/^(?:[a-z]|(?:[0-9\\ \\+\\-\\,\\.\\(\\)]+[a-z])+[0-9\\ \\+\\-\\,\\.\\(\\)]*|(?:[a-z][0-9\\ \\+\\-\\,\\.\\(\\)]+)+[a-z]?)$/')))
    if var.get('match'):
        return Js({'match_':var.get('match').get('0'),'remainder':var.get('input').callprop('substr', var.get('match').get('0').get('length'))})
    return var.get(u"null")
PyJs_anonymous_32_._set_name('anonymous')
@Js
def PyJs_anonymous_33_(input, begExcl, begIncl, endIncl, endExcl, beg2Excl, beg2Incl, end2Incl, end2Excl, combine, this, arguments, var=var):
    var = Scope({'input':input, 'begExcl':begExcl, 'begIncl':begIncl, 'endIncl':endIncl, 'endExcl':endExcl, 'beg2Excl':beg2Excl, 'beg2Incl':beg2Incl, 'end2Incl':end2Incl, 'end2Excl':end2Excl, 'combine':combine, 'this':this, 'arguments':arguments}, var)
    var.registers(['endExcl', 'end2Incl', 'group2', 'e', 'match1', 'end2Excl', '_findObserveGroups', 'match', 'input', 'combine', 'begExcl', 'begIncl', 'matchRet', 'beg2Excl', 'beg2Incl', '_match', 'endIncl'])
    @Js
    def PyJs_anonymous_34_(input, pattern, this, arguments, var=var):
        var = Scope({'input':input, 'pattern':pattern, 'this':this, 'arguments':arguments}, var)
        var.registers(['match_1', 'pattern', 'input'])
        if PyJsStrictEq(var.get('pattern',throw=False).typeof(),Js('string')):
            if PyJsStrictNeq(var.get('input').callprop('indexOf', var.get('pattern')),Js(0.0)):
                return var.get(u"null")
            return var.get('pattern')
        else:
            var.put('match_1', var.get('input').callprop('match', var.get('pattern')))
            if var.get('match_1').neg():
                return var.get(u"null")
            return var.get('match_1').get('0')
    PyJs_anonymous_34_._set_name('anonymous')
    var.put('_match', PyJs_anonymous_34_)
    @Js
    def PyJs_anonymous_35_(input, i, endChars, this, arguments, var=var):
        var = Scope({'input':input, 'i':i, 'endChars':endChars, 'this':this, 'arguments':arguments}, var)
        var.registers(['braces', 'endChars', 'a', 'input', 'match_2', 'i'])
        var.put('braces', Js(0.0))
        while (var.get('i')<var.get('input').get('length')):
            var.put('a', var.get('input').callprop('charAt', var.get('i')))
            var.put('match_2', var.get('_match')(var.get('input').callprop('substr', var.get('i')), var.get('endChars')))
            if (PyJsStrictNeq(var.get('match_2'),var.get(u"null")) and PyJsStrictEq(var.get('braces'),Js(0.0))):
                return Js({'endMatchBegin':var.get('i'),'endMatchEnd':(var.get('i')+var.get('match_2').get('length'))})
            else:
                if PyJsStrictEq(var.get('a'),Js('{')):
                    (var.put('braces',Js(var.get('braces').to_number())+Js(1))-Js(1))
                else:
                    if PyJsStrictEq(var.get('a'),Js('}')):
                        if PyJsStrictEq(var.get('braces'),Js(0.0)):
                            PyJsTempException = JsToPyException(Js([Js('ExtraCloseMissingOpen'), Js('Extra close brace or missing open brace')]))
                            raise PyJsTempException
                        else:
                            (var.put('braces',Js(var.get('braces').to_number())-Js(1))+Js(1))
            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
        if (var.get('braces')>Js(0.0)):
            return var.get(u"null")
        return var.get(u"null")
    PyJs_anonymous_35_._set_name('anonymous')
    var.put('_findObserveGroups', PyJs_anonymous_35_)
    var.put('match', var.get('_match')(var.get('input'), var.get('begExcl')))
    if PyJsStrictEq(var.get('match'),var.get(u"null")):
        return var.get(u"null")
    var.put('input', var.get('input').callprop('substr', var.get('match').get('length')))
    var.put('match', var.get('_match')(var.get('input'), var.get('begIncl')))
    if PyJsStrictEq(var.get('match'),var.get(u"null")):
        return var.get(u"null")
    var.put('e', var.get('_findObserveGroups')(var.get('input'), var.get('match').get('length'), (var.get('endIncl') or var.get('endExcl'))))
    if PyJsStrictEq(var.get('e'),var.get(u"null")):
        return var.get(u"null")
    var.put('match1', var.get('input').callprop('substring', Js(0.0), (var.get('e').get('endMatchEnd') if var.get('endIncl') else var.get('e').get('endMatchBegin'))))
    if (var.get('beg2Excl') or var.get('beg2Incl')).neg():
        return Js({'match_':var.get('match1'),'remainder':var.get('input').callprop('substr', var.get('e').get('endMatchEnd'))})
    else:
        var.put('group2', var.get(u"this").callprop('findObserveGroups', var.get('input').callprop('substr', var.get('e').get('endMatchEnd')), var.get('beg2Excl'), var.get('beg2Incl'), var.get('end2Incl'), var.get('end2Excl')))
        if PyJsStrictEq(var.get('group2'),var.get(u"null")):
            return var.get(u"null")
        var.put('matchRet', Js([var.get('match1'), var.get('group2').get('match_')]))
        return Js({'match_':(var.get('matchRet').callprop('join', Js('')) if var.get('combine') else var.get('matchRet')),'remainder':var.get('group2').get('remainder')})
PyJs_anonymous_33_._set_name('anonymous')
@Js
def PyJs_anonymous_36_(m, input, this, arguments, var=var):
    var = Scope({'m':m, 'input':input, 'this':this, 'arguments':arguments}, var)
    var.registers(['m', 'input', 'match', 'pattern'])
    var.put('pattern', var.get('_mhchemParser').get('patterns').get('patterns').get(var.get('m')))
    if PyJsStrictEq(var.get('pattern'),var.get('undefined')):
        PyJsTempException = JsToPyException(Js([Js('MhchemBugP'), ((Js('mhchem bug P. Please report. (')+var.get('m'))+Js(')'))]))
        raise PyJsTempException
    else:
        if PyJsStrictEq(var.get('pattern',throw=False).typeof(),Js('function')):
            return var.get('_mhchemParser').get('patterns').get('patterns').callprop(var.get('m'), var.get('input'))
        else:
            var.put('match', var.get('input').callprop('match', var.get('pattern')))
            if var.get('match'):
                if (var.get('match').get('length')>Js(2.0)):
                    return Js({'match_':var.get('match').callprop('slice', Js(1.0)),'remainder':var.get('input').callprop('substr', var.get('match').get('0').get('length'))})
                else:
                    return Js({'match_':(var.get('match').get('1') or var.get('match').get('0')),'remainder':var.get('input').callprop('substr', var.get('match').get('0').get('length'))})
            return var.get(u"null")
PyJs_anonymous_36_._set_name('anonymous')
@Js
def PyJs_anonymous_37_(buffer, m, this, arguments, var=var):
    var = Scope({'buffer':buffer, 'm':m, 'this':this, 'arguments':arguments}, var)
    var.registers(['buffer', 'm'])
    var.get('buffer').put('a', ((var.get('buffer').get('a') or Js(''))+var.get('m')))
    return var.get('undefined')
PyJs_anonymous_37_._set_name('anonymous')
@Js
def PyJs_anonymous_38_(buffer, m, this, arguments, var=var):
    var = Scope({'buffer':buffer, 'm':m, 'this':this, 'arguments':arguments}, var)
    var.registers(['buffer', 'm'])
    var.get('buffer').put('b', ((var.get('buffer').get('b') or Js(''))+var.get('m')))
    return var.get('undefined')
PyJs_anonymous_38_._set_name('anonymous')
@Js
def PyJs_anonymous_39_(buffer, m, this, arguments, var=var):
    var = Scope({'buffer':buffer, 'm':m, 'this':this, 'arguments':arguments}, var)
    var.registers(['buffer', 'm'])
    var.get('buffer').put('p', ((var.get('buffer').get('p') or Js(''))+var.get('m')))
    return var.get('undefined')
PyJs_anonymous_39_._set_name('anonymous')
@Js
def PyJs_anonymous_40_(buffer, m, this, arguments, var=var):
    var = Scope({'buffer':buffer, 'm':m, 'this':this, 'arguments':arguments}, var)
    var.registers(['buffer', 'm'])
    var.get('buffer').put('o', ((var.get('buffer').get('o') or Js(''))+var.get('m')))
    return var.get('undefined')
PyJs_anonymous_40_._set_name('anonymous')
@Js
def PyJs_anonymous_41_(buffer, m, this, arguments, var=var):
    var = Scope({'buffer':buffer, 'm':m, 'this':this, 'arguments':arguments}, var)
    var.registers(['buffer', 'm'])
    var.get('buffer').put('q', ((var.get('buffer').get('q') or Js(''))+var.get('m')))
    return var.get('undefined')
PyJs_anonymous_41_._set_name('anonymous')
@Js
def PyJs_anonymous_42_(buffer, m, this, arguments, var=var):
    var = Scope({'buffer':buffer, 'm':m, 'this':this, 'arguments':arguments}, var)
    var.registers(['buffer', 'm'])
    var.get('buffer').put('d', ((var.get('buffer').get('d') or Js(''))+var.get('m')))
    return var.get('undefined')
PyJs_anonymous_42_._set_name('anonymous')
@Js
def PyJs_anonymous_43_(buffer, m, this, arguments, var=var):
    var = Scope({'buffer':buffer, 'm':m, 'this':this, 'arguments':arguments}, var)
    var.registers(['buffer', 'm'])
    var.get('buffer').put('rm', ((var.get('buffer').get('rm') or Js(''))+var.get('m')))
    return var.get('undefined')
PyJs_anonymous_43_._set_name('anonymous')
@Js
def PyJs_anonymous_44_(buffer, m, this, arguments, var=var):
    var = Scope({'buffer':buffer, 'm':m, 'this':this, 'arguments':arguments}, var)
    var.registers(['buffer', 'm'])
    var.get('buffer').put('text_', ((var.get('buffer').get('text_') or Js(''))+var.get('m')))
    return var.get('undefined')
PyJs_anonymous_44_._set_name('anonymous')
@Js
def PyJs_anonymous_45_(_buffer, _m, a, this, arguments, var=var):
    var = Scope({'_buffer':_buffer, '_m':_m, 'a':a, 'this':this, 'arguments':arguments}, var)
    var.registers(['a', '_m', '_buffer'])
    return Js({'type_':var.get('a')})
PyJs_anonymous_45_._set_name('anonymous')
@Js
def PyJs_anonymous_46_(_buffer, m, a, this, arguments, var=var):
    var = Scope({'_buffer':_buffer, 'm':m, 'a':a, 'this':this, 'arguments':arguments}, var)
    var.registers(['a', '_buffer', 'm'])
    return Js({'type_':var.get('a'),'p1':var.get('m')})
PyJs_anonymous_46_._set_name('anonymous')
@Js
def PyJs_anonymous_47_(_buffer, m, a, this, arguments, var=var):
    var = Scope({'_buffer':_buffer, 'm':m, 'a':a, 'this':this, 'arguments':arguments}, var)
    var.registers(['a', '_buffer', 'm'])
    return Js({'type_':var.get('a'),'p1':var.get('m').get('0'),'p2':var.get('m').get('1')})
PyJs_anonymous_47_._set_name('anonymous')
@Js
def PyJs_anonymous_48_(_buffer, m, this, arguments, var=var):
    var = Scope({'_buffer':_buffer, 'm':m, 'this':this, 'arguments':arguments}, var)
    var.registers(['_buffer', 'm'])
    return var.get('m')
PyJs_anonymous_48_._set_name('anonymous')
@Js
def PyJs_anonymous_49_(_buffer, _m, a, this, arguments, var=var):
    var = Scope({'_buffer':_buffer, '_m':_m, 'a':a, 'this':this, 'arguments':arguments}, var)
    var.registers(['a', '_m', '_buffer'])
    return var.get('a')
PyJs_anonymous_49_._set_name('anonymous')
@Js
def PyJs_anonymous_50_(_buffer, m, this, arguments, var=var):
    var = Scope({'_buffer':_buffer, 'm':m, 'this':this, 'arguments':arguments}, var)
    var.registers(['_buffer', 'm'])
    return Js({'type_':Js('rm'),'p1':var.get('m')})
PyJs_anonymous_50_._set_name('anonymous')
@Js
def PyJs_anonymous_51_(_buffer, m, this, arguments, var=var):
    var = Scope({'_buffer':_buffer, 'm':m, 'this':this, 'arguments':arguments}, var)
    var.registers(['_buffer', 'm'])
    return var.get('_mhchemParser').callprop('go', var.get('m'), Js('text'))
PyJs_anonymous_51_._set_name('anonymous')
@Js
def PyJs_anonymous_52_(_buffer, m, this, arguments, var=var):
    var = Scope({'_buffer':_buffer, 'm':m, 'this':this, 'arguments':arguments}, var)
    var.registers(['_buffer', 'm'])
    return var.get('_mhchemParser').callprop('go', var.get('m'), Js('tex-math'))
PyJs_anonymous_52_._set_name('anonymous')
@Js
def PyJs_anonymous_53_(_buffer, m, this, arguments, var=var):
    var = Scope({'_buffer':_buffer, 'm':m, 'this':this, 'arguments':arguments}, var)
    var.registers(['_buffer', 'm'])
    return var.get('_mhchemParser').callprop('go', var.get('m'), Js('tex-math tight'))
PyJs_anonymous_53_._set_name('anonymous')
@Js
def PyJs_anonymous_54_(_buffer, m, k, this, arguments, var=var):
    var = Scope({'_buffer':_buffer, 'm':m, 'k':k, 'this':this, 'arguments':arguments}, var)
    var.registers(['k', '_buffer', 'm'])
    return Js({'type_':Js('bond'),'kind_':(var.get('k') or var.get('m'))})
PyJs_anonymous_54_._set_name('anonymous')
@Js
def PyJs_anonymous_55_(_buffer, m, this, arguments, var=var):
    var = Scope({'_buffer':_buffer, 'm':m, 'this':this, 'arguments':arguments}, var)
    var.registers(['_buffer', 'm'])
    return Js({'type_':Js('color0'),'color':var.get('m')})
PyJs_anonymous_55_._set_name('anonymous')
@Js
def PyJs_anonymous_56_(_buffer, m, this, arguments, var=var):
    var = Scope({'_buffer':_buffer, 'm':m, 'this':this, 'arguments':arguments}, var)
    var.registers(['_buffer', 'm'])
    return var.get('_mhchemParser').callprop('go', var.get('m'), Js('ce'))
PyJs_anonymous_56_._set_name('anonymous')
@Js
def PyJs_anonymous_57_(_buffer, m, this, arguments, var=var):
    var = Scope({'_buffer':_buffer, 'm':m, 'this':this, 'arguments':arguments}, var)
    var.registers(['_buffer', 'm'])
    return var.get('_mhchemParser').callprop('go', var.get('m'), Js('pu'))
PyJs_anonymous_57_._set_name('anonymous')
@Js
def PyJs_anonymous_58_(_buffer, m, this, arguments, var=var):
    var = Scope({'_buffer':_buffer, 'm':m, 'this':this, 'arguments':arguments}, var)
    var.registers(['n', 'ret', '_buffer', 'm'])
    var.put('ret', Js([]))
    if var.get('m').callprop('match', JsRegExp('/^[+\\-]/')):
        var.get('ret').callprop('push', var.get('m').callprop('substr', Js(0.0), Js(1.0)))
        var.put('m', var.get('m').callprop('substr', Js(1.0)))
    var.put('n', var.get('m').callprop('match', JsRegExp('/^([0-9]+|\\$[a-z]\\$|[a-z])\\/([0-9]+)(\\$[a-z]\\$|[a-z])?$/')))
    var.get('n').put('1', var.get('n').get('1').callprop('replace', JsRegExp('/\\$/g'), Js('')))
    var.get('ret').callprop('push', Js({'type_':Js('frac'),'p1':var.get('n').get('1'),'p2':var.get('n').get('2')}))
    if var.get('n').get('3'):
        var.get('n').put('3', var.get('n').get('3').callprop('replace', JsRegExp('/\\$/g'), Js('')))
        var.get('ret').callprop('push', Js({'type_':Js('tex-math'),'p1':var.get('n').get('3')}))
    return var.get('ret')
PyJs_anonymous_58_._set_name('anonymous')
@Js
def PyJs_anonymous_59_(_buffer, m, this, arguments, var=var):
    var = Scope({'_buffer':_buffer, 'm':m, 'this':this, 'arguments':arguments}, var)
    var.registers(['_buffer', 'm'])
    return var.get('_mhchemParser').callprop('go', var.get('m'), Js('9,9'))
PyJs_anonymous_59_._set_name('anonymous')
def PyJs_LONG_60_(var=var):
    return var.get('_mhchemCreateTransitions')(Js({'empty':Js({'0':Js({'action_':Js('copy')})}),'\\ce{(...)}':Js({'0':Js({'action_':Js([Js({'type_':Js('write'),'option':Js('{')}), Js('ce'), Js({'type_':Js('write'),'option':Js('}')})])})}),'\\pu{(...)}':Js({'0':Js({'action_':Js([Js({'type_':Js('write'),'option':Js('{')}), Js('pu'), Js({'type_':Js('write'),'option':Js('}')})])})}),'else':Js({'0':Js({'action_':Js('copy')})})}))
def PyJs_LONG_61_(var=var):
    return var.get('_mhchemCreateTransitions')(Js({'empty':Js({'*':Js({'action_':Js('output')})}),'else':Js({'0|1|2':Js({'action_':Js('beginsWithBond=false'),'revisit':Js(True),'toContinue':Js(True)})}),'oxidation$':Js({'0':Js({'action_':Js('oxidation-output')})}),'CMT':Js({'r':Js({'action_':Js('rdt='),'nextState':Js('rt')}),'rd':Js({'action_':Js('rqt='),'nextState':Js('rdt')})}),'arrowUpDown':Js({'0|1|2|as':Js({'action_':Js([Js('sb=false'), Js('output'), Js('operator')]),'nextState':Js('1')})}),'uprightEntities':Js({'0|1|2':Js({'action_':Js([Js('o='), Js('output')]),'nextState':Js('1')})}),'orbital':Js({'0|1|2|3':Js({'action_':Js('o='),'nextState':Js('o')})}),'->':Js({'0|1|2|3':Js({'action_':Js('r='),'nextState':Js('r')}),'a|as':Js({'action_':Js([Js('output'), Js('r=')]),'nextState':Js('r')}),'*':Js({'action_':Js([Js('output'), Js('r=')]),'nextState':Js('r')})}),'+':Js({'o':Js({'action_':Js('d= kv'),'nextState':Js('d')}),'d|D':Js({'action_':Js('d='),'nextState':Js('d')}),'q':Js({'action_':Js('d='),'nextState':Js('qd')}),'qd|qD':Js({'action_':Js('d='),'nextState':Js('qd')}),'dq':Js({'action_':Js([Js('output'), Js('d=')]),'nextState':Js('d')}),'3':Js({'action_':Js([Js('sb=false'), Js('output'), Js('operator')]),'nextState':Js('0')})}),'amount':Js({'0|2':Js({'action_':Js('a='),'nextState':Js('a')})}),'pm-operator':Js({'0|1|2|a|as':Js({'action_':Js([Js('sb=false'), Js('output'), Js({'type_':Js('operator'),'option':Js('\\pm')})]),'nextState':Js('0')})}),'operator':Js({'0|1|2|a|as':Js({'action_':Js([Js('sb=false'), Js('output'), Js('operator')]),'nextState':Js('0')})}),'-$':Js({'o|q':Js({'action_':Js([Js('charge or bond'), Js('output')]),'nextState':Js('qd')}),'d':Js({'action_':Js('d='),'nextState':Js('d')}),'D':Js({'action_':Js([Js('output'), Js({'type_':Js('bond'),'option':Js('-')})]),'nextState':Js('3')}),'q':Js({'action_':Js('d='),'nextState':Js('qd')}),'qd':Js({'action_':Js('d='),'nextState':Js('qd')}),'qD|dq':Js({'action_':Js([Js('output'), Js({'type_':Js('bond'),'option':Js('-')})]),'nextState':Js('3')})}),'-9':Js({'3|o':Js({'action_':Js([Js('output'), Js({'type_':Js('insert'),'option':Js('hyphen')})]),'nextState':Js('3')})}),'- orbital overlap':Js({'o':Js({'action_':Js([Js('output'), Js({'type_':Js('insert'),'option':Js('hyphen')})]),'nextState':Js('2')}),'d':Js({'action_':Js([Js('output'), Js({'type_':Js('insert'),'option':Js('hyphen')})]),'nextState':Js('2')})}),'-':Js({'0|1|2':Js({'action_':Js([Js({'type_':Js('output'),'option':Js(1.0)}), Js('beginsWithBond=true'), Js({'type_':Js('bond'),'option':Js('-')})]),'nextState':Js('3')}),'3':Js({'action_':Js({'type_':Js('bond'),'option':Js('-')})}),'a':Js({'action_':Js([Js('output'), Js({'type_':Js('insert'),'option':Js('hyphen')})]),'nextState':Js('2')}),'as':Js({'action_':Js([Js({'type_':Js('output'),'option':Js(2.0)}), Js({'type_':Js('bond'),'option':Js('-')})]),'nextState':Js('3')}),'b':Js({'action_':Js('b=')}),'o':Js({'action_':Js({'type_':Js('- after o/d'),'option':Js(False)}),'nextState':Js('2')}),'q':Js({'action_':Js({'type_':Js('- after o/d'),'option':Js(False)}),'nextState':Js('2')}),'d|qd|dq':Js({'action_':Js({'type_':Js('- after o/d'),'option':Js(True)}),'nextState':Js('2')}),'D|qD|p':Js({'action_':Js([Js('output'), Js({'type_':Js('bond'),'option':Js('-')})]),'nextState':Js('3')})}),'amount2':Js({'1|3':Js({'action_':Js('a='),'nextState':Js('a')})}),'letters':Js({'0|1|2|3|a|as|b|p|bp|o':Js({'action_':Js('o='),'nextState':Js('o')}),'q|dq':Js({'action_':Js([Js('output'), Js('o=')]),'nextState':Js('o')}),'d|D|qd|qD':Js({'action_':Js('o after d'),'nextState':Js('o')})}),'digits':Js({'o':Js({'action_':Js('q='),'nextState':Js('q')}),'d|D':Js({'action_':Js('q='),'nextState':Js('dq')}),'q':Js({'action_':Js([Js('output'), Js('o=')]),'nextState':Js('o')}),'a':Js({'action_':Js('o='),'nextState':Js('o')})}),'space A':Js({'b|p|bp':Js({'action_':Js([])})}),'space':Js({'a':Js({'action_':Js([]),'nextState':Js('as')}),'0':Js({'action_':Js('sb=false')}),'1|2':Js({'action_':Js('sb=true')}),'r|rt|rd|rdt|rdq':Js({'action_':Js('output'),'nextState':Js('0')}),'*':Js({'action_':Js([Js('output'), Js('sb=true')]),'nextState':Js('1')})}),'1st-level escape':Js({'1|2':Js({'action_':Js([Js('output'), Js({'type_':Js('insert+p1'),'option':Js('1st-level escape')})])}),'*':Js({'action_':Js([Js('output'), Js({'type_':Js('insert+p1'),'option':Js('1st-level escape')})]),'nextState':Js('0')})}),'[(...)]':Js({'r|rt':Js({'action_':Js('rd='),'nextState':Js('rd')}),'rd|rdt':Js({'action_':Js('rq='),'nextState':Js('rdq')})}),'...':Js({'o|d|D|dq|qd|qD':Js({'action_':Js([Js('output'), Js({'type_':Js('bond'),'option':Js('...')})]),'nextState':Js('3')}),'*':Js({'action_':Js([Js({'type_':Js('output'),'option':Js(1.0)}), Js({'type_':Js('insert'),'option':Js('ellipsis')})]),'nextState':Js('1')})}),'. __* ':Js({'*':Js({'action_':Js([Js('output'), Js({'type_':Js('insert'),'option':Js('addition compound')})]),'nextState':Js('1')})}),'state of aggregation $':Js({'*':Js({'action_':Js([Js('output'), Js('state of aggregation')]),'nextState':Js('1')})}),'{[(':Js({'a|as|o':Js({'action_':Js([Js('o='), Js('output'), Js('parenthesisLevel++')]),'nextState':Js('2')}),'0|1|2|3':Js({'action_':Js([Js('o='), Js('output'), Js('parenthesisLevel++')]),'nextState':Js('2')}),'*':Js({'action_':Js([Js('output'), Js('o='), Js('output'), Js('parenthesisLevel++')]),'nextState':Js('2')})}),')]}':Js({'0|1|2|3|b|p|bp|o':Js({'action_':Js([Js('o='), Js('parenthesisLevel--')]),'nextState':Js('o')}),'a|as|d|D|q|qd|qD|dq':Js({'action_':Js([Js('output'), Js('o='), Js('parenthesisLevel--')]),'nextState':Js('o')})}),', ':Js({'*':Js({'action_':Js([Js('output'), Js('comma')]),'nextState':Js('0')})}),'^_':Js({'*':Js({'action_':Js([])})}),'^{(...)}|^($...$)':Js({'0|1|2|as':Js({'action_':Js('b='),'nextState':Js('b')}),'p':Js({'action_':Js('b='),'nextState':Js('bp')}),'3|o':Js({'action_':Js('d= kv'),'nextState':Js('D')}),'q':Js({'action_':Js('d='),'nextState':Js('qD')}),'d|D|qd|qD|dq':Js({'action_':Js([Js('output'), Js('d=')]),'nextState':Js('D')})}),"^a|^\\x{}{}|^\\x{}|^\\x|'":Js({'0|1|2|as':Js({'action_':Js('b='),'nextState':Js('b')}),'p':Js({'action_':Js('b='),'nextState':Js('bp')}),'3|o':Js({'action_':Js('d= kv'),'nextState':Js('d')}),'q':Js({'action_':Js('d='),'nextState':Js('qd')}),'d|qd|D|qD':Js({'action_':Js('d=')}),'dq':Js({'action_':Js([Js('output'), Js('d=')]),'nextState':Js('d')})}),'_{(state of aggregation)}$':Js({'d|D|q|qd|qD|dq':Js({'action_':Js([Js('output'), Js('q=')]),'nextState':Js('q')})}),'_{(...)}|_($...$)|_9|_\\x{}{}|_\\x{}|_\\x':Js({'0|1|2|as':Js({'action_':Js('p='),'nextState':Js('p')}),'b':Js({'action_':Js('p='),'nextState':Js('bp')}),'3|o':Js({'action_':Js('q='),'nextState':Js('q')}),'d|D':Js({'action_':Js('q='),'nextState':Js('dq')}),'q|qd|qD|dq':Js({'action_':Js([Js('output'), Js('q=')]),'nextState':Js('q')})}),'=<>':Js({'0|1|2|3|a|as|o|q|d|D|qd|qD|dq':Js({'action_':Js([Js({'type_':Js('output'),'option':Js(2.0)}), Js('bond')]),'nextState':Js('3')})}),'#':Js({'0|1|2|3|a|as|o':Js({'action_':Js([Js({'type_':Js('output'),'option':Js(2.0)}), Js({'type_':Js('bond'),'option':Js('#')})]),'nextState':Js('3')})}),'{}^':Js({'*':Js({'action_':Js([Js({'type_':Js('output'),'option':Js(1.0)}), Js({'type_':Js('insert'),'option':Js('tinySkip')})]),'nextState':Js('1')})}),'{}':Js({'*':Js({'action_':Js({'type_':Js('output'),'option':Js(1.0)}),'nextState':Js('1')})}),'{...}':Js({'0|1|2|3|a|as|b|p|bp':Js({'action_':Js('o='),'nextState':Js('o')}),'o|d|D|q|qd|qD|dq':Js({'action_':Js([Js('output'), Js('o=')]),'nextState':Js('o')})}),'$...$':Js({'a':Js({'action_':Js('a=')}),'0|1|2|3|as|b|p|bp|o':Js({'action_':Js('o='),'nextState':Js('o')}),'as|o':Js({'action_':Js('o=')}),'q|d|D|qd|qD|dq':Js({'action_':Js([Js('output'), Js('o=')]),'nextState':Js('o')})}),'\\bond{(...)}':Js({'*':Js({'action_':Js([Js({'type_':Js('output'),'option':Js(2.0)}), Js('bond')]),'nextState':Js('3')})}),'\\frac{(...)}':Js({'*':Js({'action_':Js([Js({'type_':Js('output'),'option':Js(1.0)}), Js('frac-output')]),'nextState':Js('3')})}),'\\overset{(...)}':Js({'*':Js({'action_':Js([Js({'type_':Js('output'),'option':Js(2.0)}), Js('overset-output')]),'nextState':Js('3')})}),'\\underset{(...)}':Js({'*':Js({'action_':Js([Js({'type_':Js('output'),'option':Js(2.0)}), Js('underset-output')]),'nextState':Js('3')})}),'\\underbrace{(...)}':Js({'*':Js({'action_':Js([Js({'type_':Js('output'),'option':Js(2.0)}), Js('underbrace-output')]),'nextState':Js('3')})}),'\\color{(...)}{(...)}':Js({'*':Js({'action_':Js([Js({'type_':Js('output'),'option':Js(2.0)}), Js('color-output')]),'nextState':Js('3')})}),'\\color{(...)}':Js({'*':Js({'action_':Js([Js({'type_':Js('output'),'option':Js(2.0)}), Js('color0-output')])})}),'\\ce{(...)}':Js({'*':Js({'action_':Js([Js({'type_':Js('output'),'option':Js(2.0)}), Js('ce')]),'nextState':Js('3')})}),'\\,':Js({'*':Js({'action_':Js([Js({'type_':Js('output'),'option':Js(1.0)}), Js('copy')]),'nextState':Js('1')})}),'\\pu{(...)}':Js({'*':Js({'action_':Js([Js('output'), Js({'type_':Js('write'),'option':Js('{')}), Js('pu'), Js({'type_':Js('write'),'option':Js('}')})]),'nextState':Js('3')})}),'\\x{}{}|\\x{}|\\x':Js({'0|1|2|3|a|as|b|p|bp|o|c0':Js({'action_':Js([Js('o='), Js('output')]),'nextState':Js('3')}),'*':Js({'action_':Js([Js('output'), Js('o='), Js('output')]),'nextState':Js('3')})}),'others':Js({'*':Js({'action_':Js([Js({'type_':Js('output'),'option':Js(1.0)}), Js('copy')]),'nextState':Js('3')})}),'else2':Js({'a':Js({'action_':Js('a to o'),'nextState':Js('o'),'revisit':Js(True)}),'as':Js({'action_':Js([Js('output'), Js('sb=true')]),'nextState':Js('1'),'revisit':Js(True)}),'r|rt|rd|rdt|rdq':Js({'action_':Js([Js('output')]),'nextState':Js('0'),'revisit':Js(True)}),'*':Js({'action_':Js([Js('output'), Js('copy')]),'nextState':Js('3')})})}))
@Js
def PyJs_anonymous_62_(buffer, m, this, arguments, var=var):
    var = Scope({'buffer':buffer, 'm':m, 'this':this, 'arguments':arguments}, var)
    var.registers(['ret', 'buffer', 'm', 'tmp'])
    pass
    if (var.get('buffer').get('d') or Js('')).callprop('match', JsRegExp('/^[1-9][0-9]*$/')):
        var.put('tmp', var.get('buffer').get('d'))
        var.get('buffer').put('d', var.get('undefined'))
        var.put('ret', var.get(u"this").callprop('output', var.get('buffer')))
        var.get('ret').callprop('push', Js({'type_':Js('tinySkip')}))
        var.get('buffer').put('b', var.get('tmp'))
    else:
        var.put('ret', var.get(u"this").callprop('output', var.get('buffer')))
    var.get('_mhchemParser').get('actions').callprop('o=', var.get('buffer'), var.get('m'))
    return var.get('ret')
PyJs_anonymous_62_._set_name('anonymous')
@Js
def PyJs_anonymous_63_(buffer, m, this, arguments, var=var):
    var = Scope({'buffer':buffer, 'm':m, 'this':this, 'arguments':arguments}, var)
    var.registers(['buffer', 'm'])
    var.get('buffer').put('d', var.get('m'))
    var.get('buffer').put('dType', Js('kv'))
    return var.get('undefined')
PyJs_anonymous_63_._set_name('anonymous')
@Js
def PyJs_anonymous_64_(buffer, m, this, arguments, var=var):
    var = Scope({'buffer':buffer, 'm':m, 'this':this, 'arguments':arguments}, var)
    var.registers(['ret', 'buffer', 'm'])
    if var.get('buffer').get('beginsWithBond'):
        var.put('ret', Js([]))
        var.get('_mhchemParser').callprop('concatArray', var.get('ret'), var.get(u"this").callprop('output', var.get('buffer')))
        var.get('_mhchemParser').callprop('concatArray', var.get('ret'), var.get('_mhchemParser').get('actions').callprop('bond', var.get('buffer'), var.get('m'), Js('-')))
        return var.get('ret')
    else:
        var.get('buffer').put('d', var.get('m'))
        return var.get('undefined')
PyJs_anonymous_64_._set_name('anonymous')
@Js
def PyJs_anonymous_65_(buffer, m, isAfterD, this, arguments, var=var):
    var = Scope({'buffer':buffer, 'm':m, 'isAfterD':isAfterD, 'this':this, 'arguments':arguments}, var)
    var.registers(['c1', 'buffer', 'isAfterD', 'c2', 'c4', 'hyphenFollows', 'ret', 'c3', 'm'])
    var.put('c1', var.get('_mhchemParser').get('patterns').callprop('match_', Js('orbital'), (var.get('buffer').get('o') or Js(''))))
    var.put('c2', var.get('_mhchemParser').get('patterns').callprop('match_', Js('one lowercase greek letter $'), (var.get('buffer').get('o') or Js(''))))
    var.put('c3', var.get('_mhchemParser').get('patterns').callprop('match_', Js('one lowercase latin letter $'), (var.get('buffer').get('o') or Js(''))))
    var.put('c4', var.get('_mhchemParser').get('patterns').callprop('match_', Js('$one lowercase latin letter$ $'), (var.get('buffer').get('o') or Js(''))))
    var.put('hyphenFollows', (PyJsStrictEq(var.get('m'),Js('-')) and ((((var.get('c1') and PyJsStrictEq(var.get('c1').get('remainder'),Js(''))) or var.get('c2')) or var.get('c3')) or var.get('c4'))))
    if (((((((var.get('hyphenFollows') and var.get('buffer').get('a').neg()) and var.get('buffer').get('b').neg()) and var.get('buffer').get('p').neg()) and var.get('buffer').get('d').neg()) and var.get('buffer').get('q').neg()) and var.get('c1').neg()) and var.get('c3')):
        var.get('buffer').put('o', ((Js('$')+var.get('buffer').get('o'))+Js('$')))
    var.put('ret', Js([]))
    if var.get('hyphenFollows'):
        var.get('_mhchemParser').callprop('concatArray', var.get('ret'), var.get(u"this").callprop('output', var.get('buffer')))
        var.get('ret').callprop('push', Js({'type_':Js('hyphen')}))
    else:
        var.put('c1', var.get('_mhchemParser').get('patterns').callprop('match_', Js('digits'), (var.get('buffer').get('d') or Js(''))))
        if ((var.get('isAfterD') and var.get('c1')) and PyJsStrictEq(var.get('c1').get('remainder'),Js(''))):
            var.get('_mhchemParser').callprop('concatArray', var.get('ret'), var.get('_mhchemParser').get('actions').callprop('d=', var.get('buffer'), var.get('m')))
            var.get('_mhchemParser').callprop('concatArray', var.get('ret'), var.get(u"this").callprop('output', var.get('buffer')))
        else:
            var.get('_mhchemParser').callprop('concatArray', var.get('ret'), var.get(u"this").callprop('output', var.get('buffer')))
            var.get('_mhchemParser').callprop('concatArray', var.get('ret'), var.get('_mhchemParser').get('actions').callprop('bond', var.get('buffer'), var.get('m'), Js('-')))
    return var.get('ret')
PyJs_anonymous_65_._set_name('anonymous')
@Js
def PyJs_anonymous_66_(buffer, this, arguments, var=var):
    var = Scope({'buffer':buffer, 'this':this, 'arguments':arguments}, var)
    var.registers(['buffer'])
    var.get('buffer').put('o', var.get('buffer').get('a'))
    var.get('buffer').put('a', var.get('undefined'))
    return var.get('undefined')
PyJs_anonymous_66_._set_name('anonymous')
@Js
def PyJs_anonymous_67_(buffer, this, arguments, var=var):
    var = Scope({'buffer':buffer, 'this':this, 'arguments':arguments}, var)
    var.registers(['buffer'])
    var.get('buffer').put('sb', Js(True))
    return var.get('undefined')
PyJs_anonymous_67_._set_name('anonymous')
@Js
def PyJs_anonymous_68_(buffer, this, arguments, var=var):
    var = Scope({'buffer':buffer, 'this':this, 'arguments':arguments}, var)
    var.registers(['buffer'])
    var.get('buffer').put('sb', Js(False))
    return var.get('undefined')
PyJs_anonymous_68_._set_name('anonymous')
@Js
def PyJs_anonymous_69_(buffer, this, arguments, var=var):
    var = Scope({'buffer':buffer, 'this':this, 'arguments':arguments}, var)
    var.registers(['buffer'])
    var.get('buffer').put('beginsWithBond', Js(True))
    return var.get('undefined')
PyJs_anonymous_69_._set_name('anonymous')
@Js
def PyJs_anonymous_70_(buffer, this, arguments, var=var):
    var = Scope({'buffer':buffer, 'this':this, 'arguments':arguments}, var)
    var.registers(['buffer'])
    var.get('buffer').put('beginsWithBond', Js(False))
    return var.get('undefined')
PyJs_anonymous_70_._set_name('anonymous')
@Js
def PyJs_anonymous_71_(buffer, this, arguments, var=var):
    var = Scope({'buffer':buffer, 'this':this, 'arguments':arguments}, var)
    var.registers(['buffer'])
    (var.get('buffer').put('parenthesisLevel',Js(var.get('buffer').get('parenthesisLevel').to_number())+Js(1))-Js(1))
    return var.get('undefined')
PyJs_anonymous_71_._set_name('anonymous')
@Js
def PyJs_anonymous_72_(buffer, this, arguments, var=var):
    var = Scope({'buffer':buffer, 'this':this, 'arguments':arguments}, var)
    var.registers(['buffer'])
    (var.get('buffer').put('parenthesisLevel',Js(var.get('buffer').get('parenthesisLevel').to_number())-Js(1))+Js(1))
    return var.get('undefined')
PyJs_anonymous_72_._set_name('anonymous')
@Js
def PyJs_anonymous_73_(_buffer, m, this, arguments, var=var):
    var = Scope({'_buffer':_buffer, 'm':m, 'this':this, 'arguments':arguments}, var)
    var.registers(['_buffer', 'm'])
    return Js({'type_':Js('state of aggregation'),'p1':var.get('_mhchemParser').callprop('go', var.get('m'), Js('o'))})
PyJs_anonymous_73_._set_name('anonymous')
@Js
def PyJs_anonymous_74_(buffer, m, this, arguments, var=var):
    var = Scope({'buffer':buffer, 'm':m, 'this':this, 'arguments':arguments}, var)
    var.registers(['withSpace', 'a', 'buffer', 'm'])
    var.put('a', var.get('m').callprop('replace', JsRegExp('/\\s*$/'), Js('')))
    var.put('withSpace', PyJsStrictNeq(var.get('a'),var.get('m')))
    if (var.get('withSpace') and PyJsStrictEq(var.get('buffer').get('parenthesisLevel'),Js(0.0))):
        return Js({'type_':Js('comma enumeration L'),'p1':var.get('a')})
    else:
        return Js({'type_':Js('comma enumeration M'),'p1':var.get('a')})
PyJs_anonymous_74_._set_name('anonymous')
@Js
def PyJs_anonymous_75_(buffer, _m, entityFollows, this, arguments, var=var):
    var = Scope({'buffer':buffer, '_m':_m, 'entityFollows':entityFollows, 'this':this, 'arguments':arguments}, var)
    var.registers(['p', 'buffer', '_m', 'ret', 'entityFollows', 'rq', 'rd'])
    pass
    if var.get('buffer').get('r').neg():
        var.put('ret', Js([]))
        if ((((((var.get('buffer').get('a').neg() and var.get('buffer').get('b').neg()) and var.get('buffer').get('p').neg()) and var.get('buffer').get('o').neg()) and var.get('buffer').get('q').neg()) and var.get('buffer').get('d').neg()) and var.get('entityFollows').neg()):
            pass
        else:
            if var.get('buffer').get('sb'):
                var.get('ret').callprop('push', Js({'type_':Js('entitySkip')}))
            if (((((var.get('buffer').get('o').neg() and var.get('buffer').get('q').neg()) and var.get('buffer').get('d').neg()) and var.get('buffer').get('b').neg()) and var.get('buffer').get('p').neg()) and PyJsStrictNeq(var.get('entityFollows'),Js(2.0))):
                var.get('buffer').put('o', var.get('buffer').get('a'))
                var.get('buffer').put('a', var.get('undefined'))
            else:
                if (((var.get('buffer').get('o').neg() and var.get('buffer').get('q').neg()) and var.get('buffer').get('d').neg()) and (var.get('buffer').get('b') or var.get('buffer').get('p'))):
                    var.get('buffer').put('o', var.get('buffer').get('a'))
                    var.get('buffer').put('d', var.get('buffer').get('b'))
                    var.get('buffer').put('q', var.get('buffer').get('p'))
                    var.get('buffer').put('a', var.get('buffer').put('b', var.get('buffer').put('p', var.get('undefined'))))
                else:
                    if ((var.get('buffer').get('o') and PyJsStrictEq(var.get('buffer').get('dType'),Js('kv'))) and var.get('_mhchemParser').get('patterns').callprop('match_', Js('d-oxidation$'), (var.get('buffer').get('d') or Js('')))):
                        var.get('buffer').put('dType', Js('oxidation'))
                    else:
                        if ((var.get('buffer').get('o') and PyJsStrictEq(var.get('buffer').get('dType'),Js('kv'))) and var.get('buffer').get('q').neg()):
                            var.get('buffer').put('dType', var.get('undefined'))
            def PyJs_LONG_76_(var=var):
                return var.get('ret').callprop('push', Js({'type_':Js('chemfive'),'a':var.get('_mhchemParser').callprop('go', var.get('buffer').get('a'), Js('a')),'b':var.get('_mhchemParser').callprop('go', var.get('buffer').get('b'), Js('bd')),'p':var.get('_mhchemParser').callprop('go', var.get('buffer').get('p'), Js('pq')),'o':var.get('_mhchemParser').callprop('go', var.get('buffer').get('o'), Js('o')),'q':var.get('_mhchemParser').callprop('go', var.get('buffer').get('q'), Js('pq')),'d':var.get('_mhchemParser').callprop('go', var.get('buffer').get('d'), (Js('oxidation') if PyJsStrictEq(var.get('buffer').get('dType'),Js('oxidation')) else Js('bd'))),'dType':var.get('buffer').get('dType')}))
            PyJs_LONG_76_()
    else:
        var.put('rd', PyJsComma(Js(0.0), Js(None)))
        if PyJsStrictEq(var.get('buffer').get('rdt'),Js('M')):
            var.put('rd', var.get('_mhchemParser').callprop('go', var.get('buffer').get('rd'), Js('tex-math')))
        else:
            if PyJsStrictEq(var.get('buffer').get('rdt'),Js('T')):
                var.put('rd', Js([Js({'type_':Js('text'),'p1':(var.get('buffer').get('rd') or Js(''))})]))
            else:
                var.put('rd', var.get('_mhchemParser').callprop('go', var.get('buffer').get('rd'), Js('ce')))
        var.put('rq', PyJsComma(Js(0.0), Js(None)))
        if PyJsStrictEq(var.get('buffer').get('rqt'),Js('M')):
            var.put('rq', var.get('_mhchemParser').callprop('go', var.get('buffer').get('rq'), Js('tex-math')))
        else:
            if PyJsStrictEq(var.get('buffer').get('rqt'),Js('T')):
                var.put('rq', Js([Js({'type_':Js('text'),'p1':(var.get('buffer').get('rq') or Js(''))})]))
            else:
                var.put('rq', var.get('_mhchemParser').callprop('go', var.get('buffer').get('rq'), Js('ce')))
        var.put('ret', Js({'type_':Js('arrow'),'r':var.get('buffer').get('r'),'rd':var.get('rd'),'rq':var.get('rq')}))
    for PyJsTemp in var.get('buffer'):
        var.put('p', PyJsTemp)
        if (PyJsStrictNeq(var.get('p'),Js('parenthesisLevel')) and PyJsStrictNeq(var.get('p'),Js('beginsWithBond'))):
            var.get('buffer').delete(var.get('p'))
    return var.get('ret')
PyJs_anonymous_75_._set_name('anonymous')
@Js
def PyJs_anonymous_77_(_buffer, m, this, arguments, var=var):
    var = Scope({'_buffer':_buffer, 'm':m, 'this':this, 'arguments':arguments}, var)
    var.registers(['ret', '_buffer', 'm'])
    var.put('ret', Js([Js('{')]))
    var.get('_mhchemParser').callprop('concatArray', var.get('ret'), var.get('_mhchemParser').callprop('go', var.get('m'), Js('oxidation')))
    var.get('ret').callprop('push', Js('}'))
    return var.get('ret')
PyJs_anonymous_77_._set_name('anonymous')
@Js
def PyJs_anonymous_78_(_buffer, m, this, arguments, var=var):
    var = Scope({'_buffer':_buffer, 'm':m, 'this':this, 'arguments':arguments}, var)
    var.registers(['_buffer', 'm'])
    return Js({'type_':Js('frac-ce'),'p1':var.get('_mhchemParser').callprop('go', var.get('m').get('0'), Js('ce')),'p2':var.get('_mhchemParser').callprop('go', var.get('m').get('1'), Js('ce'))})
PyJs_anonymous_78_._set_name('anonymous')
@Js
def PyJs_anonymous_79_(_buffer, m, this, arguments, var=var):
    var = Scope({'_buffer':_buffer, 'm':m, 'this':this, 'arguments':arguments}, var)
    var.registers(['_buffer', 'm'])
    return Js({'type_':Js('overset'),'p1':var.get('_mhchemParser').callprop('go', var.get('m').get('0'), Js('ce')),'p2':var.get('_mhchemParser').callprop('go', var.get('m').get('1'), Js('ce'))})
PyJs_anonymous_79_._set_name('anonymous')
@Js
def PyJs_anonymous_80_(_buffer, m, this, arguments, var=var):
    var = Scope({'_buffer':_buffer, 'm':m, 'this':this, 'arguments':arguments}, var)
    var.registers(['_buffer', 'm'])
    return Js({'type_':Js('underset'),'p1':var.get('_mhchemParser').callprop('go', var.get('m').get('0'), Js('ce')),'p2':var.get('_mhchemParser').callprop('go', var.get('m').get('1'), Js('ce'))})
PyJs_anonymous_80_._set_name('anonymous')
@Js
def PyJs_anonymous_81_(_buffer, m, this, arguments, var=var):
    var = Scope({'_buffer':_buffer, 'm':m, 'this':this, 'arguments':arguments}, var)
    var.registers(['_buffer', 'm'])
    return Js({'type_':Js('underbrace'),'p1':var.get('_mhchemParser').callprop('go', var.get('m').get('0'), Js('ce')),'p2':var.get('_mhchemParser').callprop('go', var.get('m').get('1'), Js('ce'))})
PyJs_anonymous_81_._set_name('anonymous')
@Js
def PyJs_anonymous_82_(_buffer, m, this, arguments, var=var):
    var = Scope({'_buffer':_buffer, 'm':m, 'this':this, 'arguments':arguments}, var)
    var.registers(['_buffer', 'm'])
    return Js({'type_':Js('color'),'color1':var.get('m').get('0'),'color2':var.get('_mhchemParser').callprop('go', var.get('m').get('1'), Js('ce'))})
PyJs_anonymous_82_._set_name('anonymous')
@Js
def PyJs_anonymous_83_(buffer, m, this, arguments, var=var):
    var = Scope({'buffer':buffer, 'm':m, 'this':this, 'arguments':arguments}, var)
    var.registers(['buffer', 'm'])
    var.get('buffer').put('r', var.get('m'))
    return var.get('undefined')
PyJs_anonymous_83_._set_name('anonymous')
@Js
def PyJs_anonymous_84_(buffer, m, this, arguments, var=var):
    var = Scope({'buffer':buffer, 'm':m, 'this':this, 'arguments':arguments}, var)
    var.registers(['buffer', 'm'])
    var.get('buffer').put('rdt', var.get('m'))
    return var.get('undefined')
PyJs_anonymous_84_._set_name('anonymous')
@Js
def PyJs_anonymous_85_(buffer, m, this, arguments, var=var):
    var = Scope({'buffer':buffer, 'm':m, 'this':this, 'arguments':arguments}, var)
    var.registers(['buffer', 'm'])
    var.get('buffer').put('rd', var.get('m'))
    return var.get('undefined')
PyJs_anonymous_85_._set_name('anonymous')
@Js
def PyJs_anonymous_86_(buffer, m, this, arguments, var=var):
    var = Scope({'buffer':buffer, 'm':m, 'this':this, 'arguments':arguments}, var)
    var.registers(['buffer', 'm'])
    var.get('buffer').put('rqt', var.get('m'))
    return var.get('undefined')
PyJs_anonymous_86_._set_name('anonymous')
@Js
def PyJs_anonymous_87_(buffer, m, this, arguments, var=var):
    var = Scope({'buffer':buffer, 'm':m, 'this':this, 'arguments':arguments}, var)
    var.registers(['buffer', 'm'])
    var.get('buffer').put('rq', var.get('m'))
    return var.get('undefined')
PyJs_anonymous_87_._set_name('anonymous')
@Js
def PyJs_anonymous_88_(_buffer, m, p1, this, arguments, var=var):
    var = Scope({'_buffer':_buffer, 'm':m, 'p1':p1, 'this':this, 'arguments':arguments}, var)
    var.registers(['p1', '_buffer', 'm'])
    return Js({'type_':Js('operator'),'kind_':(var.get('p1') or var.get('m'))})
PyJs_anonymous_88_._set_name('anonymous')
def PyJs_LONG_89_(var=var):
    return var.get('_mhchemCreateTransitions')(Js({'empty':Js({'*':Js({'action_':Js([])})}),'1/2$':Js({'0':Js({'action_':Js('1/2')})}),'else':Js({'0':Js({'action_':Js([]),'nextState':Js('1'),'revisit':Js(True)})}),'${(...)}$__$(...)$':Js({'*':Js({'action_':Js('tex-math tight'),'nextState':Js('1')})}),',':Js({'*':Js({'action_':Js({'type_':Js('insert'),'option':Js('commaDecimal')})})}),'else2':Js({'*':Js({'action_':Js('copy')})})}))
def PyJs_LONG_90_(var=var):
    return var.get('_mhchemCreateTransitions')(Js({'empty':Js({'*':Js({'action_':Js([])})}),'1/2$':Js({'0':Js({'action_':Js('1/2')})}),'else':Js({'0':Js({'action_':Js([]),'nextState':Js('1'),'revisit':Js(True)})}),'letters':Js({'*':Js({'action_':Js('rm')})}),'\\ca':Js({'*':Js({'action_':Js({'type_':Js('insert'),'option':Js('circa')})})}),'\\pu{(...)}':Js({'*':Js({'action_':Js([Js({'type_':Js('write'),'option':Js('{')}), Js('pu'), Js({'type_':Js('write'),'option':Js('}')})])})}),'\\x{}{}|\\x{}|\\x':Js({'*':Js({'action_':Js('copy')})}),'${(...)}$__$(...)$':Js({'*':Js({'action_':Js('tex-math')})}),'{(...)}':Js({'*':Js({'action_':Js([Js({'type_':Js('write'),'option':Js('{')}), Js('text'), Js({'type_':Js('write'),'option':Js('}')})])})}),'else2':Js({'*':Js({'action_':Js('copy')})})}))
def PyJs_LONG_91_(var=var):
    return var.get('_mhchemCreateTransitions')(Js({'empty':Js({'*':Js({'action_':Js('output')})}),'{...}':Js({'*':Js({'action_':Js('text=')})}),'${(...)}$__$(...)$':Js({'*':Js({'action_':Js('tex-math')})}),'\\greek':Js({'*':Js({'action_':Js([Js('output'), Js('rm')])})}),'\\pu{(...)}':Js({'*':Js({'action_':Js([Js('output'), Js({'type_':Js('write'),'option':Js('{')}), Js('pu'), Js({'type_':Js('write'),'option':Js('}')})])})}),'\\,|\\x{}{}|\\x{}|\\x':Js({'*':Js({'action_':Js([Js('output'), Js('copy')])})}),'else':Js({'*':Js({'action_':Js('text=')})})}))
@Js
def PyJs_anonymous_92_(buffer, this, arguments, var=var):
    var = Scope({'buffer':buffer, 'this':this, 'arguments':arguments}, var)
    var.registers(['ret', 'buffer', 'p'])
    if var.get('buffer').get('text_'):
        var.put('ret', Js({'type_':Js('text'),'p1':var.get('buffer').get('text_')}))
        for PyJsTemp in var.get('buffer'):
            var.put('p', PyJsTemp)
            var.get('buffer').delete(var.get('p'))
        return var.get('ret')
    return var.get('undefined')
PyJs_anonymous_92_._set_name('anonymous')
def PyJs_LONG_93_(var=var):
    return var.get('_mhchemCreateTransitions')(Js({'empty':Js({'*':Js({'action_':Js([])})}),'state of aggregation $':Js({'*':Js({'action_':Js('state of aggregation')})}),'i$':Js({'0':Js({'action_':Js([]),'nextState':Js('!f'),'revisit':Js(True)})}),'(KV letters),':Js({'0':Js({'action_':Js('rm'),'nextState':Js('0')})}),'formula$':Js({'0':Js({'action_':Js([]),'nextState':Js('f'),'revisit':Js(True)})}),'1/2$':Js({'0':Js({'action_':Js('1/2')})}),'else':Js({'0':Js({'action_':Js([]),'nextState':Js('!f'),'revisit':Js(True)})}),'${(...)}$__$(...)$':Js({'*':Js({'action_':Js('tex-math')})}),'{(...)}':Js({'*':Js({'action_':Js('text')})}),'a-z':Js({'f':Js({'action_':Js('tex-math')})}),'letters':Js({'*':Js({'action_':Js('rm')})}),'-9.,9':Js({'*':Js({'action_':Js('9,9')})}),',':Js({'*':Js({'action_':Js({'type_':Js('insert+p1'),'option':Js('comma enumeration S')})})}),'\\color{(...)}{(...)}':Js({'*':Js({'action_':Js('color-output')})}),'\\color{(...)}':Js({'*':Js({'action_':Js('color0-output')})}),'\\ce{(...)}':Js({'*':Js({'action_':Js('ce')})}),'\\pu{(...)}':Js({'*':Js({'action_':Js([Js({'type_':Js('write'),'option':Js('{')}), Js('pu'), Js({'type_':Js('write'),'option':Js('}')})])})}),'\\,|\\x{}{}|\\x{}|\\x':Js({'*':Js({'action_':Js('copy')})}),'else2':Js({'*':Js({'action_':Js('copy')})})}))
@Js
def PyJs_anonymous_94_(_buffer, m, this, arguments, var=var):
    var = Scope({'_buffer':_buffer, 'm':m, 'this':this, 'arguments':arguments}, var)
    var.registers(['_buffer', 'm'])
    return Js({'type_':Js('state of aggregation subscript'),'p1':var.get('_mhchemParser').callprop('go', var.get('m'), Js('o'))})
PyJs_anonymous_94_._set_name('anonymous')
@Js
def PyJs_anonymous_95_(_buffer, m, this, arguments, var=var):
    var = Scope({'_buffer':_buffer, 'm':m, 'this':this, 'arguments':arguments}, var)
    var.registers(['_buffer', 'm'])
    return Js({'type_':Js('color'),'color1':var.get('m').get('0'),'color2':var.get('_mhchemParser').callprop('go', var.get('m').get('1'), Js('pq'))})
PyJs_anonymous_95_._set_name('anonymous')
def PyJs_LONG_96_(var=var):
    return var.get('_mhchemCreateTransitions')(Js({'empty':Js({'*':Js({'action_':Js([])})}),'x$':Js({'0':Js({'action_':Js([]),'nextState':Js('!f'),'revisit':Js(True)})}),'formula$':Js({'0':Js({'action_':Js([]),'nextState':Js('f'),'revisit':Js(True)})}),'else':Js({'0':Js({'action_':Js([]),'nextState':Js('!f'),'revisit':Js(True)})}),'-9.,9 no missing 0':Js({'*':Js({'action_':Js('9,9')})}),'.':Js({'*':Js({'action_':Js({'type_':Js('insert'),'option':Js('electron dot')})})}),'a-z':Js({'f':Js({'action_':Js('tex-math')})}),'x':Js({'*':Js({'action_':Js({'type_':Js('insert'),'option':Js('KV x')})})}),'letters':Js({'*':Js({'action_':Js('rm')})}),"'":Js({'*':Js({'action_':Js({'type_':Js('insert'),'option':Js('prime')})})}),'${(...)}$__$(...)$':Js({'*':Js({'action_':Js('tex-math')})}),'{(...)}':Js({'*':Js({'action_':Js('text')})}),'\\color{(...)}{(...)}':Js({'*':Js({'action_':Js('color-output')})}),'\\color{(...)}':Js({'*':Js({'action_':Js('color0-output')})}),'\\ce{(...)}':Js({'*':Js({'action_':Js('ce')})}),'\\pu{(...)}':Js({'*':Js({'action_':Js([Js({'type_':Js('write'),'option':Js('{')}), Js('pu'), Js({'type_':Js('write'),'option':Js('}')})])})}),'\\,|\\x{}{}|\\x{}|\\x':Js({'*':Js({'action_':Js('copy')})}),'else2':Js({'*':Js({'action_':Js('copy')})})}))
@Js
def PyJs_anonymous_97_(_buffer, m, this, arguments, var=var):
    var = Scope({'_buffer':_buffer, 'm':m, 'this':this, 'arguments':arguments}, var)
    var.registers(['_buffer', 'm'])
    return Js({'type_':Js('color'),'color1':var.get('m').get('0'),'color2':var.get('_mhchemParser').callprop('go', var.get('m').get('1'), Js('bd'))})
PyJs_anonymous_97_._set_name('anonymous')
@Js
def PyJs_anonymous_98_(_buffer, m, this, arguments, var=var):
    var = Scope({'_buffer':_buffer, 'm':m, 'this':this, 'arguments':arguments}, var)
    var.registers(['_buffer', 'm'])
    return Js({'type_':Js('roman numeral'),'p1':var.get('m')})
PyJs_anonymous_98_._set_name('anonymous')
def PyJs_LONG_99_(var=var):
    return var.get('_mhchemCreateTransitions')(Js({'empty':Js({'*':Js({'action_':Js('output')})}),'\\ce{(...)}':Js({'*':Js({'action_':Js([Js('output'), Js('ce')])})}),'\\pu{(...)}':Js({'*':Js({'action_':Js([Js('output'), Js({'type_':Js('write'),'option':Js('{')}), Js('pu'), Js({'type_':Js('write'),'option':Js('}')})])})}),'{...}|\\,|\\x{}{}|\\x{}|\\x':Js({'*':Js({'action_':Js('o=')})}),'else':Js({'*':Js({'action_':Js('o=')})})}))
@Js
def PyJs_anonymous_100_(buffer, this, arguments, var=var):
    var = Scope({'buffer':buffer, 'this':this, 'arguments':arguments}, var)
    var.registers(['ret', 'buffer', 'p'])
    if var.get('buffer').get('o'):
        var.put('ret', Js({'type_':Js('tex-math'),'p1':var.get('buffer').get('o')}))
        for PyJsTemp in var.get('buffer'):
            var.put('p', PyJsTemp)
            var.get('buffer').delete(var.get('p'))
        return var.get('ret')
    return var.get('undefined')
PyJs_anonymous_100_._set_name('anonymous')
def PyJs_LONG_101_(var=var):
    return var.get('_mhchemCreateTransitions')(Js({'empty':Js({'*':Js({'action_':Js('output')})}),'\\ce{(...)}':Js({'*':Js({'action_':Js([Js('output'), Js('ce')])})}),'\\pu{(...)}':Js({'*':Js({'action_':Js([Js('output'), Js({'type_':Js('write'),'option':Js('{')}), Js('pu'), Js({'type_':Js('write'),'option':Js('}')})])})}),'{...}|\\,|\\x{}{}|\\x{}|\\x':Js({'*':Js({'action_':Js('o=')})}),'-|+':Js({'*':Js({'action_':Js('tight operator')})}),'else':Js({'*':Js({'action_':Js('o=')})})}))
@Js
def PyJs_anonymous_102_(buffer, m, this, arguments, var=var):
    var = Scope({'buffer':buffer, 'm':m, 'this':this, 'arguments':arguments}, var)
    var.registers(['buffer', 'm'])
    var.get('buffer').put('o', ((((var.get('buffer').get('o') or Js(''))+Js('{'))+var.get('m'))+Js('}')))
    return var.get('undefined')
PyJs_anonymous_102_._set_name('anonymous')
@Js
def PyJs_anonymous_103_(buffer, this, arguments, var=var):
    var = Scope({'buffer':buffer, 'this':this, 'arguments':arguments}, var)
    var.registers(['ret', 'buffer', 'p'])
    if var.get('buffer').get('o'):
        var.put('ret', Js({'type_':Js('tex-math'),'p1':var.get('buffer').get('o')}))
        for PyJsTemp in var.get('buffer'):
            var.put('p', PyJsTemp)
            var.get('buffer').delete(var.get('p'))
        return var.get('ret')
    return var.get('undefined')
PyJs_anonymous_103_._set_name('anonymous')
@Js
def PyJs_anonymous_104_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers([])
    return Js({'type_':Js('commaDecimal')})
PyJs_anonymous_104_._set_name('anonymous')
def PyJs_LONG_105_(var=var):
    return var.get('_mhchemCreateTransitions')(Js({'empty':Js({'*':Js({'action_':Js('output')})}),'space$':Js({'*':Js({'action_':Js([Js('output'), Js('space')])})}),'{[(|)]}':Js({'0|a':Js({'action_':Js('copy')})}),'(-)(9)^(-9)':Js({'0':Js({'action_':Js('number^'),'nextState':Js('a')})}),'(-)(9.,9)(e)(99)':Js({'0':Js({'action_':Js('enumber'),'nextState':Js('a')})}),'space':Js({'0|a':Js({'action_':Js([])})}),'pm-operator':Js({'0|a':Js({'action_':Js({'type_':Js('operator'),'option':Js('\\pm')}),'nextState':Js('0')})}),'operator':Js({'0|a':Js({'action_':Js('copy'),'nextState':Js('0')})}),'//':Js({'d':Js({'action_':Js('o='),'nextState':Js('/')})}),'/':Js({'d':Js({'action_':Js('o='),'nextState':Js('/')})}),'{...}|else':Js({'0|d':Js({'action_':Js('d='),'nextState':Js('d')}),'a':Js({'action_':Js([Js('space'), Js('d=')]),'nextState':Js('d')}),'/|q':Js({'action_':Js('q='),'nextState':Js('q')})})}))
@Js
def PyJs_anonymous_106_(_buffer, m, this, arguments, var=var):
    var = Scope({'_buffer':_buffer, 'm':m, 'this':this, 'arguments':arguments}, var)
    var.registers(['ret', '_buffer', 'm'])
    var.put('ret', Js([]))
    if (PyJsStrictEq(var.get('m').get('0'),Js('+-')) or PyJsStrictEq(var.get('m').get('0'),Js('+/-'))):
        var.get('ret').callprop('push', Js('\\pm '))
    else:
        if var.get('m').get('0'):
            var.get('ret').callprop('push', var.get('m').get('0'))
    if var.get('m').get('1'):
        var.get('_mhchemParser').callprop('concatArray', var.get('ret'), var.get('_mhchemParser').callprop('go', var.get('m').get('1'), Js('pu-9,9')))
        if var.get('m').get('2'):
            if var.get('m').get('2').callprop('match', JsRegExp('/[,.]/')):
                var.get('_mhchemParser').callprop('concatArray', var.get('ret'), var.get('_mhchemParser').callprop('go', var.get('m').get('2'), Js('pu-9,9')))
            else:
                var.get('ret').callprop('push', var.get('m').get('2'))
        if (var.get('m').get('3') or var.get('m').get('4')):
            if (PyJsStrictEq(var.get('m').get('3'),Js('e')) or PyJsStrictEq(var.get('m').get('4'),Js('*'))):
                var.get('ret').callprop('push', Js({'type_':Js('cdot')}))
            else:
                var.get('ret').callprop('push', Js({'type_':Js('times')}))
    if var.get('m').get('5'):
        var.get('ret').callprop('push', ((Js('10^{')+var.get('m').get('5'))+Js('}')))
    return var.get('ret')
PyJs_anonymous_106_._set_name('anonymous')
@Js
def PyJs_anonymous_107_(_buffer, m, this, arguments, var=var):
    var = Scope({'_buffer':_buffer, 'm':m, 'this':this, 'arguments':arguments}, var)
    var.registers(['ret', '_buffer', 'm'])
    var.put('ret', Js([]))
    if (PyJsStrictEq(var.get('m').get('0'),Js('+-')) or PyJsStrictEq(var.get('m').get('0'),Js('+/-'))):
        var.get('ret').callprop('push', Js('\\pm '))
    else:
        if var.get('m').get('0'):
            var.get('ret').callprop('push', var.get('m').get('0'))
    var.get('_mhchemParser').callprop('concatArray', var.get('ret'), var.get('_mhchemParser').callprop('go', var.get('m').get('1'), Js('pu-9,9')))
    var.get('ret').callprop('push', ((Js('^{')+var.get('m').get('2'))+Js('}')))
    return var.get('ret')
PyJs_anonymous_107_._set_name('anonymous')
@Js
def PyJs_anonymous_108_(_buffer, m, p1, this, arguments, var=var):
    var = Scope({'_buffer':_buffer, 'm':m, 'p1':p1, 'this':this, 'arguments':arguments}, var)
    var.registers(['p1', '_buffer', 'm'])
    return Js({'type_':Js('operator'),'kind_':(var.get('p1') or var.get('m'))})
PyJs_anonymous_108_._set_name('anonymous')
@Js
def PyJs_anonymous_109_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers([])
    return Js({'type_':Js('pu-space-1')})
PyJs_anonymous_109_._set_name('anonymous')
@Js
def PyJs_anonymous_110_(buffer, this, arguments, var=var):
    var = Scope({'buffer':buffer, 'this':this, 'arguments':arguments}, var)
    var.registers(['p', 'buffer', 'ret', 'b5', 'md', 'mq'])
    pass
    var.put('md', var.get('_mhchemParser').get('patterns').callprop('match_', Js('{(...)}'), (var.get('buffer').get('d') or Js(''))))
    if (var.get('md') and PyJsStrictEq(var.get('md').get('remainder'),Js(''))):
        var.get('buffer').put('d', var.get('md').get('match_'))
    var.put('mq', var.get('_mhchemParser').get('patterns').callprop('match_', Js('{(...)}'), (var.get('buffer').get('q') or Js(''))))
    if (var.get('mq') and PyJsStrictEq(var.get('mq').get('remainder'),Js(''))):
        var.get('buffer').put('q', var.get('mq').get('match_'))
    if var.get('buffer').get('d'):
        var.get('buffer').put('d', var.get('buffer').get('d').callprop('replace', JsRegExp('/\\u00B0C|\\^oC|\\^{o}C/g'), Js('{}^{\\circ}C')))
        var.get('buffer').put('d', var.get('buffer').get('d').callprop('replace', JsRegExp('/\\u00B0F|\\^oF|\\^{o}F/g'), Js('{}^{\\circ}F')))
    if var.get('buffer').get('q'):
        var.get('buffer').put('q', var.get('buffer').get('q').callprop('replace', JsRegExp('/\\u00B0C|\\^oC|\\^{o}C/g'), Js('{}^{\\circ}C')))
        var.get('buffer').put('q', var.get('buffer').get('q').callprop('replace', JsRegExp('/\\u00B0F|\\^oF|\\^{o}F/g'), Js('{}^{\\circ}F')))
        var.put('b5', Js({'d':var.get('_mhchemParser').callprop('go', var.get('buffer').get('d'), Js('pu')),'q':var.get('_mhchemParser').callprop('go', var.get('buffer').get('q'), Js('pu'))}))
        if PyJsStrictEq(var.get('buffer').get('o'),Js('//')):
            var.put('ret', Js({'type_':Js('pu-frac'),'p1':var.get('b5').get('d'),'p2':var.get('b5').get('q')}))
        else:
            var.put('ret', var.get('b5').get('d'))
            if ((var.get('b5').get('d').get('length')>Js(1.0)) or (var.get('b5').get('q').get('length')>Js(1.0))):
                var.get('ret').callprop('push', Js({'type_':Js(' / ')}))
            else:
                var.get('ret').callprop('push', Js({'type_':Js('/')}))
            var.get('_mhchemParser').callprop('concatArray', var.get('ret'), var.get('b5').get('q'))
    else:
        var.put('ret', var.get('_mhchemParser').callprop('go', var.get('buffer').get('d'), Js('pu-2')))
    for PyJsTemp in var.get('buffer'):
        var.put('p', PyJsTemp)
        var.get('buffer').delete(var.get('p'))
    return var.get('ret')
PyJs_anonymous_110_._set_name('anonymous')
def PyJs_LONG_111_(var=var):
    return var.get('_mhchemCreateTransitions')(Js({'empty':Js({'*':Js({'action_':Js('output')})}),'*':Js({'*':Js({'action_':Js([Js('output'), Js('cdot')]),'nextState':Js('0')})}),'\\x':Js({'*':Js({'action_':Js('rm=')})}),'space':Js({'*':Js({'action_':Js([Js('output'), Js('space')]),'nextState':Js('0')})}),'^{(...)}|^(-1)':Js({'1':Js({'action_':Js('^(-1)')})}),'-9.,9':Js({'0':Js({'action_':Js('rm='),'nextState':Js('0')}),'1':Js({'action_':Js('^(-1)'),'nextState':Js('0')})}),'{...}|else':Js({'*':Js({'action_':Js('rm='),'nextState':Js('1')})})}))
@Js
def PyJs_anonymous_112_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers([])
    return Js({'type_':Js('tight cdot')})
PyJs_anonymous_112_._set_name('anonymous')
@Js
def PyJs_anonymous_113_(buffer, m, this, arguments, var=var):
    var = Scope({'buffer':buffer, 'm':m, 'this':this, 'arguments':arguments}, var)
    var.registers(['buffer', 'm'])
    var.get('buffer').put('rm', ((Js('^{')+var.get('m'))+Js('}')), '+')
    return var.get('undefined')
PyJs_anonymous_113_._set_name('anonymous')
@Js
def PyJs_anonymous_114_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers([])
    return Js({'type_':Js('pu-space-2')})
PyJs_anonymous_114_._set_name('anonymous')
@Js
def PyJs_anonymous_115_(buffer, this, arguments, var=var):
    var = Scope({'buffer':buffer, 'this':this, 'arguments':arguments}, var)
    var.registers(['ret', 'p', 'mrm', 'buffer'])
    var.put('ret', Js([]))
    if var.get('buffer').get('rm'):
        var.put('mrm', var.get('_mhchemParser').get('patterns').callprop('match_', Js('{(...)}'), (var.get('buffer').get('rm') or Js(''))))
        if (var.get('mrm') and PyJsStrictEq(var.get('mrm').get('remainder'),Js(''))):
            var.put('ret', var.get('_mhchemParser').callprop('go', var.get('mrm').get('match_'), Js('pu')))
        else:
            var.put('ret', Js({'type_':Js('rm'),'p1':var.get('buffer').get('rm')}))
    for PyJsTemp in var.get('buffer'):
        var.put('p', PyJsTemp)
        var.get('buffer').delete(var.get('p'))
    return var.get('ret')
PyJs_anonymous_115_._set_name('anonymous')
@Js
def PyJs_anonymous_116_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers([])
    return Js({'type_':Js('commaDecimal')})
PyJs_anonymous_116_._set_name('anonymous')
@Js
def PyJs_anonymous_117_(buffer, this, arguments, var=var):
    var = Scope({'buffer':buffer, 'this':this, 'arguments':arguments}, var)
    var.registers(['p', 'buffer', 'ret', 'a', 'i'])
    var.put('ret', Js([]))
    var.get('buffer').put('text_', (var.get('buffer').get('text_') or Js('')))
    if (var.get('buffer').get('text_').get('length')>Js(4.0)):
        var.put('a', (var.get('buffer').get('text_').get('length')%Js(3.0)))
        if PyJsStrictEq(var.get('a'),Js(0.0)):
            var.put('a', Js(3.0))
        #for JS loop
        var.put('i', (var.get('buffer').get('text_').get('length')-Js(3.0)))
        while (var.get('i')>Js(0.0)):
            try:
                var.get('ret').callprop('push', var.get('buffer').get('text_').callprop('substr', var.get('i'), Js(3.0)))
                var.get('ret').callprop('push', Js({'type_':Js('1000 separator')}))
            finally:
                    var.put('i', Js(3.0), '-')
        var.get('ret').callprop('push', var.get('buffer').get('text_').callprop('substr', Js(0.0), var.get('a')))
        var.get('ret').callprop('reverse')
    else:
        var.get('ret').callprop('push', var.get('buffer').get('text_'))
    for PyJsTemp in var.get('buffer'):
        var.put('p', PyJsTemp)
        var.get('buffer').delete(var.get('p'))
    return var.get('ret')
PyJs_anonymous_117_._set_name('anonymous')
@Js
def PyJs_anonymous_118_(buffer, this, arguments, var=var):
    var = Scope({'buffer':buffer, 'this':this, 'arguments':arguments}, var)
    var.registers(['p', 'buffer', 'ret', 'a', 'i'])
    var.put('ret', Js([]))
    var.get('buffer').put('text_', (var.get('buffer').get('text_') or Js('')))
    if (var.get('buffer').get('text_').get('length')>Js(4.0)):
        var.put('a', (var.get('buffer').get('text_').get('length')-Js(3.0)))
        var.put('i', PyJsComma(Js(0.0), Js(None)))
        #for JS loop
        var.put('i', Js(0.0))
        while (var.get('i')<var.get('a')):
            try:
                var.get('ret').callprop('push', var.get('buffer').get('text_').callprop('substr', var.get('i'), Js(3.0)))
                var.get('ret').callprop('push', Js({'type_':Js('1000 separator')}))
            finally:
                    var.put('i', Js(3.0), '+')
        var.get('ret').callprop('push', var.get('buffer').get('text_').callprop('substr', var.get('i')))
    else:
        var.get('ret').callprop('push', var.get('buffer').get('text_'))
    for PyJsTemp in var.get('buffer'):
        var.put('p', PyJsTemp)
        var.get('buffer').delete(var.get('p'))
    return var.get('ret')
PyJs_anonymous_118_._set_name('anonymous')
var.put('_mhchemParser', Js({'go':PyJs_anonymous_2_,'concatArray':PyJs_anonymous_3_,'patterns':Js({'patterns':Js({'empty':JsRegExp('/^$/'),'else':JsRegExp('/^./'),'else2':JsRegExp('/^./'),'space':JsRegExp('/^\\s/'),'space A':JsRegExp('/^\\s(?=[A-Z\\\\$])/'),'space$':JsRegExp('/^\\s$/'),'a-z':JsRegExp('/^[a-z]/'),'x':JsRegExp('/^x/'),'x$':JsRegExp('/^x$/'),'i$':JsRegExp('/^i$/'),'letters':JsRegExp('/^(?:[a-zA-Z\\u03B1-\\u03C9\\u0391-\\u03A9?@]|(?:\\\\(?:alpha|beta|gamma|delta|epsilon|zeta|eta|theta|iota|kappa|lambda|mu|nu|xi|omicron|pi|rho|sigma|tau|upsilon|phi|chi|psi|omega|Gamma|Delta|Theta|Lambda|Xi|Pi|Sigma|Upsilon|Phi|Psi|Omega)(?:\\s+|\\{\\}|(?![a-zA-Z]))))+/'),'\\greek':JsRegExp('/^\\\\(?:alpha|beta|gamma|delta|epsilon|zeta|eta|theta|iota|kappa|lambda|mu|nu|xi|omicron|pi|rho|sigma|tau|upsilon|phi|chi|psi|omega|Gamma|Delta|Theta|Lambda|Xi|Pi|Sigma|Upsilon|Phi|Psi|Omega)(?:\\s+|\\{\\}|(?![a-zA-Z]))/'),'one lowercase latin letter $':JsRegExp('/^(?:([a-z])(?:$|[^a-zA-Z]))$/'),'$one lowercase latin letter$ $':JsRegExp('/^\\$(?:([a-z])(?:$|[^a-zA-Z]))\\$$/'),'one lowercase greek letter $':JsRegExp('/^(?:\\$?[\\u03B1-\\u03C9]\\$?|\\$?\\\\(?:alpha|beta|gamma|delta|epsilon|zeta|eta|theta|iota|kappa|lambda|mu|nu|xi|omicron|pi|rho|sigma|tau|upsilon|phi|chi|psi|omega)\\s*\\$?)(?:\\s+|\\{\\}|(?![a-zA-Z]))$/'),'digits':JsRegExp('/^[0-9]+/'),'-9.,9':JsRegExp('/^[+\\-]?(?:[0-9]+(?:[,.][0-9]+)?|[0-9]*(?:\\.[0-9]+))/'),'-9.,9 no missing 0':JsRegExp('/^[+\\-]?[0-9]+(?:[.,][0-9]+)?/'),'(-)(9.,9)(e)(99)':PyJs_anonymous_4_,'(-)(9)^(-9)':JsRegExp('/^(\\+\\-|\\+\\/\\-|\\+|\\-|\\\\pm\\s?)?([0-9]+(?:[,.][0-9]+)?|[0-9]*(?:\\.[0-9]+)?)\\^([+\\-]?[0-9]+|\\{[+\\-]?[0-9]+\\})/'),'state of aggregation $':PyJs_anonymous_5_,'_{(state of aggregation)}$':JsRegExp('/^_\\{(\\([a-z]{1,3}\\))\\}/'),'{[(':JsRegExp('/^(?:\\\\\\{|\\[|\\()/'),')]}':JsRegExp('/^(?:\\)|\\]|\\\\\\})/'),', ':JsRegExp('/^[,;]\\s*/'),',':JsRegExp('/^[,;]/'),'.':JsRegExp('/^[.]/'),'. __* ':JsRegExp('/^([.\\u22C5\\u00B7\\u2022]|[*])\\s*/'),'...':JsRegExp('/^\\.\\.\\.(?=$|[^.])/'),'^{(...)}':PyJs_anonymous_6_,'^($...$)':PyJs_anonymous_7_,'^a':JsRegExp('/^\\^([0-9]+|[^\\\\_])/'),'^\\x{}{}':PyJs_anonymous_8_,'^\\x{}':PyJs_anonymous_9_,'^\\x':JsRegExp('/^\\^(\\\\[a-zA-Z]+)\\s*/'),'^(-1)':JsRegExp('/^\\^(-?\\d+)/'),"'":JsRegExp("/^'/"),'_{(...)}':PyJs_anonymous_10_,'_($...$)':PyJs_anonymous_11_,'_9':JsRegExp('/^_([+\\-]?[0-9]+|[^\\\\])/'),'_\\x{}{}':PyJs_anonymous_12_,'_\\x{}':PyJs_anonymous_13_,'_\\x':JsRegExp('/^_(\\\\[a-zA-Z]+)\\s*/'),'^_':JsRegExp('/^(?:\\^(?=_)|\\_(?=\\^)|[\\^_]$)/'),'{}^':JsRegExp('/^\\{\\}(?=\\^)/'),'{}':JsRegExp('/^\\{\\}/'),'{...}':PyJs_anonymous_14_,'{(...)}':PyJs_anonymous_15_,'$...$':PyJs_anonymous_16_,'${(...)}$__$(...)$':PyJs_anonymous_17_,'=<>':JsRegExp('/^[=<>]/'),'#':JsRegExp('/^[#\\u2261]/'),'+':JsRegExp('/^\\+/'),'-$':JsRegExp('/^-(?=[\\s_},;\\]/]|$|\\([a-z]+\\))/'),'-9':JsRegExp('/^-(?=[0-9])/'),'- orbital overlap':JsRegExp('/^-(?=(?:[spd]|sp)(?:$|[\\s,;\\)\\]\\}]))/'),'-':JsRegExp('/^-/'),'pm-operator':JsRegExp('/^(?:\\\\pm|\\$\\\\pm\\$|\\+-|\\+\\/-)/'),'operator':JsRegExp('/^(?:\\+|(?:[\\-=<>]|<<|>>|\\\\approx|\\$\\\\approx\\$)(?=\\s|$|-?[0-9]))/'),'arrowUpDown':JsRegExp('/^(?:v|\\(v\\)|\\^|\\(\\^\\))(?=$|[\\s,;\\)\\]\\}])/'),'\\bond{(...)}':PyJs_anonymous_18_,'->':JsRegExp('/^(?:<->|<-->|->|<-|<=>>|<<=>|<=>)/'),'CMT':JsRegExp('/^[CMT](?=\\[)/'),'[(...)]':PyJs_anonymous_19_,'1st-level escape':JsRegExp('/^(&|\\\\\\\\|\\\\hline)\\s*/'),'\\,':JsRegExp('/^(?:\\\\[,\\ ;:])/'),'\\x{}{}':PyJs_anonymous_20_,'\\x{}':PyJs_anonymous_21_,'\\ca':JsRegExp('/^\\\\ca(?:\\s+|(?![a-zA-Z]))/'),'\\x':JsRegExp('/^(?:\\\\[a-zA-Z]+\\s*|\\\\[_&{}%])/'),'orbital':JsRegExp('/^(?:[0-9]{1,2}[spdfgh]|[0-9]{0,2}sp)(?=$|[^a-zA-Z])/'),'others':JsRegExp('/^[\\/~|]/'),'\\frac{(...)}':PyJs_anonymous_22_,'\\overset{(...)}':PyJs_anonymous_23_,'\\underset{(...)}':PyJs_anonymous_24_,'\\underbrace{(...)}':PyJs_anonymous_25_,'\\color{(...)}':PyJs_anonymous_26_,'\\color{(...)}{(...)}':PyJs_anonymous_27_,'\\ce{(...)}':PyJs_anonymous_28_,'\\pu{(...)}':PyJs_anonymous_29_,'oxidation$':JsRegExp('/^(?:[+-][IVX]+|\\\\pm\\s*0|\\$\\\\pm\\$\\s*0)$/'),'d-oxidation$':JsRegExp('/^(?:[+-]?\\s?[IVX]+|\\\\pm\\s*0|\\$\\\\pm\\$\\s*0)$/'),'roman numeral':JsRegExp('/^[IVX]+/'),'1/2$':JsRegExp('/^[+\\-]?(?:[0-9]+|\\$[a-z]\\$|[a-z])\\/[0-9]+(?:\\$[a-z]\\$|[a-z])?$/'),'amount':PyJs_anonymous_30_,'amount2':PyJs_anonymous_31_,'(KV letters),':JsRegExp('/^(?:[A-Z][a-z]{0,2}|i)(?=,)/'),'formula$':PyJs_anonymous_32_,'uprightEntities':JsRegExp('/^(?:pH|pOH|pC|pK|iPr|iBu)(?=$|[^a-zA-Z])/'),'/':JsRegExp('/^\\s*(\\/)\\s*/'),'//':JsRegExp('/^\\s*(\\/\\/)\\s*/'),'*':JsRegExp('/^\\s*[*.]\\s*/')}),'findObserveGroups':PyJs_anonymous_33_,'match_':PyJs_anonymous_36_}),'actions':Js({'a=':PyJs_anonymous_37_,'b=':PyJs_anonymous_38_,'p=':PyJs_anonymous_39_,'o=':PyJs_anonymous_40_,'q=':PyJs_anonymous_41_,'d=':PyJs_anonymous_42_,'rm=':PyJs_anonymous_43_,'text=':PyJs_anonymous_44_,'insert':PyJs_anonymous_45_,'insert+p1':PyJs_anonymous_46_,'insert+p1+p2':PyJs_anonymous_47_,'copy':PyJs_anonymous_48_,'write':PyJs_anonymous_49_,'rm':PyJs_anonymous_50_,'text':PyJs_anonymous_51_,'tex-math':PyJs_anonymous_52_,'tex-math tight':PyJs_anonymous_53_,'bond':PyJs_anonymous_54_,'color0-output':PyJs_anonymous_55_,'ce':PyJs_anonymous_56_,'pu':PyJs_anonymous_57_,'1/2':PyJs_anonymous_58_,'9,9':PyJs_anonymous_59_}),'stateMachines':Js({'tex':Js({'transitions':PyJs_LONG_60_(),'actions':Js({})}),'ce':Js({'transitions':PyJs_LONG_61_(),'actions':Js({'o after d':PyJs_anonymous_62_,'d= kv':PyJs_anonymous_63_,'charge or bond':PyJs_anonymous_64_,'- after o/d':PyJs_anonymous_65_,'a to o':PyJs_anonymous_66_,'sb=true':PyJs_anonymous_67_,'sb=false':PyJs_anonymous_68_,'beginsWithBond=true':PyJs_anonymous_69_,'beginsWithBond=false':PyJs_anonymous_70_,'parenthesisLevel++':PyJs_anonymous_71_,'parenthesisLevel--':PyJs_anonymous_72_,'state of aggregation':PyJs_anonymous_73_,'comma':PyJs_anonymous_74_,'output':PyJs_anonymous_75_,'oxidation-output':PyJs_anonymous_77_,'frac-output':PyJs_anonymous_78_,'overset-output':PyJs_anonymous_79_,'underset-output':PyJs_anonymous_80_,'underbrace-output':PyJs_anonymous_81_,'color-output':PyJs_anonymous_82_,'r=':PyJs_anonymous_83_,'rdt=':PyJs_anonymous_84_,'rd=':PyJs_anonymous_85_,'rqt=':PyJs_anonymous_86_,'rq=':PyJs_anonymous_87_,'operator':PyJs_anonymous_88_})}),'a':Js({'transitions':PyJs_LONG_89_(),'actions':Js({})}),'o':Js({'transitions':PyJs_LONG_90_(),'actions':Js({})}),'text':Js({'transitions':PyJs_LONG_91_(),'actions':Js({'output':PyJs_anonymous_92_})}),'pq':Js({'transitions':PyJs_LONG_93_(),'actions':Js({'state of aggregation':PyJs_anonymous_94_,'color-output':PyJs_anonymous_95_})}),'bd':Js({'transitions':PyJs_LONG_96_(),'actions':Js({'color-output':PyJs_anonymous_97_})}),'oxidation':Js({'transitions':var.get('_mhchemCreateTransitions')(Js({'empty':Js({'*':Js({'action_':Js([])})}),'roman numeral':Js({'*':Js({'action_':Js('roman-numeral')})}),'${(...)}$__$(...)$':Js({'*':Js({'action_':Js('tex-math')})}),'else':Js({'*':Js({'action_':Js('copy')})})})),'actions':Js({'roman-numeral':PyJs_anonymous_98_})}),'tex-math':Js({'transitions':PyJs_LONG_99_(),'actions':Js({'output':PyJs_anonymous_100_})}),'tex-math tight':Js({'transitions':PyJs_LONG_101_(),'actions':Js({'tight operator':PyJs_anonymous_102_,'output':PyJs_anonymous_103_})}),'9,9':Js({'transitions':var.get('_mhchemCreateTransitions')(Js({'empty':Js({'*':Js({'action_':Js([])})}),',':Js({'*':Js({'action_':Js('comma')})}),'else':Js({'*':Js({'action_':Js('copy')})})})),'actions':Js({'comma':PyJs_anonymous_104_})}),'pu':Js({'transitions':PyJs_LONG_105_(),'actions':Js({'enumber':PyJs_anonymous_106_,'number^':PyJs_anonymous_107_,'operator':PyJs_anonymous_108_,'space':PyJs_anonymous_109_,'output':PyJs_anonymous_110_})}),'pu-2':Js({'transitions':PyJs_LONG_111_(),'actions':Js({'cdot':PyJs_anonymous_112_,'^(-1)':PyJs_anonymous_113_,'space':PyJs_anonymous_114_,'output':PyJs_anonymous_115_})}),'pu-9,9':Js({'transitions':var.get('_mhchemCreateTransitions')(Js({'empty':Js({'0':Js({'action_':Js('output-0')}),'o':Js({'action_':Js('output-o')})}),',':Js({'0':Js({'action_':Js([Js('output-0'), Js('comma')]),'nextState':Js('o')})}),'.':Js({'0':Js({'action_':Js([Js('output-0'), Js('copy')]),'nextState':Js('o')})}),'else':Js({'*':Js({'action_':Js('text=')})})})),'actions':Js({'comma':PyJs_anonymous_116_,'output-0':PyJs_anonymous_117_,'output-o':PyJs_anonymous_118_})})})}))
@Js
def PyJs_anonymous_119_(input, addOuterBraces, this, arguments, var=var):
    var = Scope({'input':input, 'addOuterBraces':addOuterBraces, 'this':this, 'arguments':arguments}, var)
    var.registers(['res', 'addOuterBraces', 'input', 'inputi', 'cee', 'i'])
    if var.get('input').neg():
        return Js('')
    var.put('res', Js(''))
    var.put('cee', Js(False))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('input').get('length')):
        try:
            var.put('inputi', var.get('input').get(var.get('i')))
            if PyJsStrictEq(var.get('inputi',throw=False).typeof(),Js('string')):
                var.put('res', var.get('inputi'), '+')
            else:
                var.put('res', var.get('_mhchemTexify').callprop('_go2', var.get('inputi')), '+')
                if PyJsStrictEq(var.get('inputi').get('type_'),Js('1st-level escape')):
                    var.put('cee', Js(True))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    if ((var.get('addOuterBraces') and var.get('cee').neg()) and var.get('res')):
        var.put('res', ((Js('{')+var.get('res'))+Js('}')))
    return var.get('res')
PyJs_anonymous_119_._set_name('anonymous')
@Js
def PyJs_anonymous_120_(input, this, arguments, var=var):
    var = Scope({'input':input, 'this':this, 'arguments':arguments}, var)
    var.registers(['input'])
    return var.get('_mhchemTexify').callprop('go', var.get('input'), Js(False))
PyJs_anonymous_120_._set_name('anonymous')
@Js
def PyJs_anonymous_121_(buf, this, arguments, var=var):
    var = Scope({'buf':buf, 'this':this, 'arguments':arguments}, var)
    var.registers(['res', 'arrow', 'b5', 'b6', 'd', 'buf', 'c'])
    pass
    while 1:
        SWITCHED = False
        CONDITION = (var.get('buf').get('type_'))
        if SWITCHED or PyJsStrictEq(CONDITION, Js('chemfive')):
            SWITCHED = True
            var.put('res', Js(''))
            var.put('b5', Js({'a':var.get('_mhchemTexify').callprop('_goInner', var.get('buf').get('a')),'b':var.get('_mhchemTexify').callprop('_goInner', var.get('buf').get('b')),'p':var.get('_mhchemTexify').callprop('_goInner', var.get('buf').get('p')),'o':var.get('_mhchemTexify').callprop('_goInner', var.get('buf').get('o')),'q':var.get('_mhchemTexify').callprop('_goInner', var.get('buf').get('q')),'d':var.get('_mhchemTexify').callprop('_goInner', var.get('buf').get('d'))}))
            if var.get('b5').get('a'):
                if var.get('b5').get('a').callprop('match', JsRegExp('/^[+\\-]/')):
                    var.get('b5').put('a', ((Js('{')+var.get('b5').get('a'))+Js('}')))
                var.put('res', (var.get('b5').get('a')+Js('\\,')), '+')
            if (var.get('b5').get('b') or var.get('b5').get('p')):
                var.put('res', Js('{\\vphantom{A}}'), '+')
                var.put('res', ((((Js('^{\\hphantom{')+(var.get('b5').get('b') or Js('')))+Js('}}_{\\hphantom{'))+(var.get('b5').get('p') or Js('')))+Js('}}')), '+')
                var.put('res', Js('\\mkern-1.5mu'), '+')
                var.put('res', Js('{\\vphantom{A}}'), '+')
                var.put('res', ((Js('^{\\smash[t]{\\vphantom{2}}\\llap{')+(var.get('b5').get('b') or Js('')))+Js('}}')), '+')
                var.put('res', ((Js('_{\\vphantom{2}\\llap{\\smash[t]{')+(var.get('b5').get('p') or Js('')))+Js('}}}')), '+')
            if var.get('b5').get('o'):
                if var.get('b5').get('o').callprop('match', JsRegExp('/^[+\\-]/')):
                    var.get('b5').put('o', ((Js('{')+var.get('b5').get('o'))+Js('}')))
                var.put('res', var.get('b5').get('o'), '+')
            if PyJsStrictEq(var.get('buf').get('dType'),Js('kv')):
                if (var.get('b5').get('d') or var.get('b5').get('q')):
                    var.put('res', Js('{\\vphantom{A}}'), '+')
                if var.get('b5').get('d'):
                    var.put('res', ((Js('^{')+var.get('b5').get('d'))+Js('}')), '+')
                if var.get('b5').get('q'):
                    var.put('res', ((Js('_{\\smash[t]{')+var.get('b5').get('q'))+Js('}}')), '+')
            else:
                if PyJsStrictEq(var.get('buf').get('dType'),Js('oxidation')):
                    if var.get('b5').get('d'):
                        var.put('res', Js('{\\vphantom{A}}'), '+')
                        var.put('res', ((Js('^{')+var.get('b5').get('d'))+Js('}')), '+')
                    if var.get('b5').get('q'):
                        var.put('res', Js('{\\vphantom{A}}'), '+')
                        var.put('res', ((Js('_{\\smash[t]{')+var.get('b5').get('q'))+Js('}}')), '+')
                else:
                    if var.get('b5').get('q'):
                        var.put('res', Js('{\\vphantom{A}}'), '+')
                        var.put('res', ((Js('_{\\smash[t]{')+var.get('b5').get('q'))+Js('}}')), '+')
                    if var.get('b5').get('d'):
                        var.put('res', Js('{\\vphantom{A}}'), '+')
                        var.put('res', ((Js('^{')+var.get('b5').get('d'))+Js('}')), '+')
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js('rm')):
            SWITCHED = True
            var.put('res', ((Js('\\mathrm{')+var.get('buf').get('p1'))+Js('}')))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js('text')):
            SWITCHED = True
            if var.get('buf').get('p1').callprop('match', JsRegExp('/[\\^_]/')):
                var.get('buf').put('p1', var.get('buf').get('p1').callprop('replace', Js(' '), Js('~')).callprop('replace', Js('-'), Js('\\text{-}')))
                var.put('res', ((Js('\\mathrm{')+var.get('buf').get('p1'))+Js('}')))
            else:
                var.put('res', ((Js('\\text{')+var.get('buf').get('p1'))+Js('}')))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js('roman numeral')):
            SWITCHED = True
            var.put('res', ((Js('\\mathrm{')+var.get('buf').get('p1'))+Js('}')))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js('state of aggregation')):
            SWITCHED = True
            var.put('res', (Js('\\mskip2mu ')+var.get('_mhchemTexify').callprop('_goInner', var.get('buf').get('p1'))))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js('state of aggregation subscript')):
            SWITCHED = True
            var.put('res', (Js('\\mskip1mu ')+var.get('_mhchemTexify').callprop('_goInner', var.get('buf').get('p1'))))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js('bond')):
            SWITCHED = True
            var.put('res', var.get('_mhchemTexify').callprop('_getBond', var.get('buf').get('kind_')))
            if var.get('res').neg():
                PyJsTempException = JsToPyException(Js([Js('MhchemErrorBond'), ((Js('mhchem Error. Unknown bond type (')+var.get('buf').get('kind_'))+Js(')'))]))
                raise PyJsTempException
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js('frac')):
            SWITCHED = True
            var.put('c', ((((Js('\\frac{')+var.get('buf').get('p1'))+Js('}{'))+var.get('buf').get('p2'))+Js('}')))
            var.put('res', ((((((((Js('\\mathchoice{\\textstyle')+var.get('c'))+Js('}{'))+var.get('c'))+Js('}{'))+var.get('c'))+Js('}{'))+var.get('c'))+Js('}')))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js('pu-frac')):
            SWITCHED = True
            var.put('d', ((((Js('\\frac{')+var.get('_mhchemTexify').callprop('_goInner', var.get('buf').get('p1')))+Js('}{'))+var.get('_mhchemTexify').callprop('_goInner', var.get('buf').get('p2')))+Js('}')))
            var.put('res', ((((((((Js('\\mathchoice{\\textstyle')+var.get('d'))+Js('}{'))+var.get('d'))+Js('}{'))+var.get('d'))+Js('}{'))+var.get('d'))+Js('}')))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js('tex-math')):
            SWITCHED = True
            var.put('res', (var.get('buf').get('p1')+Js(' ')))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js('frac-ce')):
            SWITCHED = True
            var.put('res', ((((Js('\\frac{')+var.get('_mhchemTexify').callprop('_goInner', var.get('buf').get('p1')))+Js('}{'))+var.get('_mhchemTexify').callprop('_goInner', var.get('buf').get('p2')))+Js('}')))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js('overset')):
            SWITCHED = True
            var.put('res', ((((Js('\\overset{')+var.get('_mhchemTexify').callprop('_goInner', var.get('buf').get('p1')))+Js('}{'))+var.get('_mhchemTexify').callprop('_goInner', var.get('buf').get('p2')))+Js('}')))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js('underset')):
            SWITCHED = True
            var.put('res', ((((Js('\\underset{')+var.get('_mhchemTexify').callprop('_goInner', var.get('buf').get('p1')))+Js('}{'))+var.get('_mhchemTexify').callprop('_goInner', var.get('buf').get('p2')))+Js('}')))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js('underbrace')):
            SWITCHED = True
            var.put('res', ((((Js('\\underbrace{')+var.get('_mhchemTexify').callprop('_goInner', var.get('buf').get('p1')))+Js('}_{'))+var.get('_mhchemTexify').callprop('_goInner', var.get('buf').get('p2')))+Js('}')))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js('color')):
            SWITCHED = True
            var.put('res', ((((Js('{\\color{')+var.get('buf').get('color1'))+Js('}{'))+var.get('_mhchemTexify').callprop('_goInner', var.get('buf').get('color2')))+Js('}}')))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js('color0')):
            SWITCHED = True
            var.put('res', ((Js('\\color{')+var.get('buf').get('color'))+Js('}')))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js('arrow')):
            SWITCHED = True
            var.put('b6', Js({'rd':var.get('_mhchemTexify').callprop('_goInner', var.get('buf').get('rd')),'rq':var.get('_mhchemTexify').callprop('_goInner', var.get('buf').get('rq'))}))
            var.put('arrow', var.get('_mhchemTexify').callprop('_getArrow', var.get('buf').get('r')))
            if (var.get('b6').get('rd') or var.get('b6').get('rq')):
                if (((PyJsStrictEq(var.get('buf').get('r'),Js('<=>')) or PyJsStrictEq(var.get('buf').get('r'),Js('<=>>'))) or PyJsStrictEq(var.get('buf').get('r'),Js('<<=>'))) or PyJsStrictEq(var.get('buf').get('r'),Js('<-->'))):
                    var.put('arrow', (Js('\\long')+var.get('arrow')))
                    if var.get('b6').get('rd'):
                        var.put('arrow', ((((Js('\\overset{')+var.get('b6').get('rd'))+Js('}{'))+var.get('arrow'))+Js('}')))
                    if var.get('b6').get('rq'):
                        if PyJsStrictEq(var.get('buf').get('r'),Js('<-->')):
                            var.put('arrow', ((((Js('\\underset{\\lower2mu{')+var.get('b6').get('rq'))+Js('}}{'))+var.get('arrow'))+Js('}')))
                        else:
                            var.put('arrow', ((((Js('\\underset{\\lower6mu{')+var.get('b6').get('rq'))+Js('}}{'))+var.get('arrow'))+Js('}')))
                    var.put('arrow', ((Js(' {}\\mathrel{')+var.get('arrow'))+Js('}{} ')))
                else:
                    if var.get('b6').get('rq'):
                        var.put('arrow', ((Js('[{')+var.get('b6').get('rq'))+Js('}]')), '+')
                    var.put('arrow', ((Js('{')+var.get('b6').get('rd'))+Js('}')), '+')
                    var.put('arrow', ((Js(' {}\\mathrel{\\x')+var.get('arrow'))+Js('}{} ')))
            else:
                var.put('arrow', ((Js(' {}\\mathrel{\\long')+var.get('arrow'))+Js('}{} ')))
            var.put('res', var.get('arrow'))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js('operator')):
            SWITCHED = True
            var.put('res', var.get('_mhchemTexify').callprop('_getOperator', var.get('buf').get('kind_')))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js('1st-level escape')):
            SWITCHED = True
            var.put('res', (var.get('buf').get('p1')+Js(' ')))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js('space')):
            SWITCHED = True
            var.put('res', Js(' '))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js('tinySkip')):
            SWITCHED = True
            var.put('res', Js('\\mkern2mu'))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js('entitySkip')):
            SWITCHED = True
            var.put('res', Js('~'))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js('pu-space-1')):
            SWITCHED = True
            var.put('res', Js('~'))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js('pu-space-2')):
            SWITCHED = True
            var.put('res', Js('\\mkern3mu '))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js('1000 separator')):
            SWITCHED = True
            var.put('res', Js('\\mkern2mu '))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js('commaDecimal')):
            SWITCHED = True
            var.put('res', Js('{,}'))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js('comma enumeration L')):
            SWITCHED = True
            var.put('res', ((Js('{')+var.get('buf').get('p1'))+Js('}\\mkern6mu ')))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js('comma enumeration M')):
            SWITCHED = True
            var.put('res', ((Js('{')+var.get('buf').get('p1'))+Js('}\\mkern3mu ')))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js('comma enumeration S')):
            SWITCHED = True
            var.put('res', ((Js('{')+var.get('buf').get('p1'))+Js('}\\mkern1mu ')))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js('hyphen')):
            SWITCHED = True
            var.put('res', Js('\\text{-}'))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js('addition compound')):
            SWITCHED = True
            var.put('res', Js('\\,{\\cdot}\\,'))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js('electron dot')):
            SWITCHED = True
            var.put('res', Js('\\mkern1mu \\bullet\\mkern1mu '))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js('KV x')):
            SWITCHED = True
            var.put('res', Js('{\\times}'))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js('prime')):
            SWITCHED = True
            var.put('res', Js('\\prime '))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js('cdot')):
            SWITCHED = True
            var.put('res', Js('\\cdot '))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js('tight cdot')):
            SWITCHED = True
            var.put('res', Js('\\mkern1mu{\\cdot}\\mkern1mu '))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js('times')):
            SWITCHED = True
            var.put('res', Js('\\times '))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js('circa')):
            SWITCHED = True
            var.put('res', Js('{\\sim}'))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js('^')):
            SWITCHED = True
            var.put('res', Js('uparrow'))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js('v')):
            SWITCHED = True
            var.put('res', Js('downarrow'))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js('ellipsis')):
            SWITCHED = True
            var.put('res', Js('\\ldots '))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js('/')):
            SWITCHED = True
            var.put('res', Js('/'))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js(' / ')):
            SWITCHED = True
            var.put('res', Js('\\,/\\,'))
            break
        if True:
            SWITCHED = True
            var.get('assertNever')(var.get('buf'))
            PyJsTempException = JsToPyException(Js([Js('MhchemBugT'), Js('mhchem bug T. Please report.')]))
            raise PyJsTempException
        SWITCHED = True
        break
    return var.get('res')
PyJs_anonymous_121_._set_name('anonymous')
@Js
def PyJs_anonymous_122_(a, this, arguments, var=var):
    var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
    var.registers(['a'])
    while 1:
        SWITCHED = False
        CONDITION = (var.get('a'))
        if SWITCHED or PyJsStrictEq(CONDITION, Js('->')):
            SWITCHED = True
            return Js('rightarrow')
        if SWITCHED or PyJsStrictEq(CONDITION, Js('<-')):
            SWITCHED = True
            return Js('leftarrow')
        if SWITCHED or PyJsStrictEq(CONDITION, Js('<->')):
            SWITCHED = True
            return Js('leftrightarrow')
        if SWITCHED or PyJsStrictEq(CONDITION, Js('<-->')):
            SWITCHED = True
            return Js('leftrightarrows')
        if SWITCHED or PyJsStrictEq(CONDITION, Js('<=>')):
            SWITCHED = True
            return Js('rightleftharpoons')
        if SWITCHED or PyJsStrictEq(CONDITION, Js('<=>>')):
            SWITCHED = True
            return Js('Rightleftharpoons')
        if SWITCHED or PyJsStrictEq(CONDITION, Js('<<=>')):
            SWITCHED = True
            return Js('Leftrightharpoons')
        if True:
            SWITCHED = True
            var.get('assertNever')(var.get('a'))
            PyJsTempException = JsToPyException(Js([Js('MhchemBugT'), Js('mhchem bug T. Please report.')]))
            raise PyJsTempException
        SWITCHED = True
        break
PyJs_anonymous_122_._set_name('anonymous')
@Js
def PyJs_anonymous_123_(a, this, arguments, var=var):
    var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
    var.registers(['a'])
    while 1:
        SWITCHED = False
        CONDITION = (var.get('a'))
        if SWITCHED or PyJsStrictEq(CONDITION, Js('-')):
            SWITCHED = True
            return Js('{-}')
        if SWITCHED or PyJsStrictEq(CONDITION, Js('1')):
            SWITCHED = True
            return Js('{-}')
        if SWITCHED or PyJsStrictEq(CONDITION, Js('=')):
            SWITCHED = True
            return Js('{=}')
        if SWITCHED or PyJsStrictEq(CONDITION, Js('2')):
            SWITCHED = True
            return Js('{=}')
        if SWITCHED or PyJsStrictEq(CONDITION, Js('#')):
            SWITCHED = True
            return Js('{\\equiv}')
        if SWITCHED or PyJsStrictEq(CONDITION, Js('3')):
            SWITCHED = True
            return Js('{\\equiv}')
        if SWITCHED or PyJsStrictEq(CONDITION, Js('~')):
            SWITCHED = True
            return Js('{\\tripledash}')
        if SWITCHED or PyJsStrictEq(CONDITION, Js('~-')):
            SWITCHED = True
            return Js('{\\rlap{\\lower.1em{-}}\\raise.1em{\\tripledash}}')
        if SWITCHED or PyJsStrictEq(CONDITION, Js('~=')):
            SWITCHED = True
            return Js('{\\rlap{\\lower.2em{-}}\\rlap{\\raise.2em{\\tripledash}}-}')
        if SWITCHED or PyJsStrictEq(CONDITION, Js('~--')):
            SWITCHED = True
            return Js('{\\rlap{\\lower.2em{-}}\\rlap{\\raise.2em{\\tripledash}}-}')
        if SWITCHED or PyJsStrictEq(CONDITION, Js('-~-')):
            SWITCHED = True
            return Js('{\\rlap{\\lower.2em{-}}\\rlap{\\raise.2em{-}}\\tripledash}')
        if SWITCHED or PyJsStrictEq(CONDITION, Js('...')):
            SWITCHED = True
            return Js('{{\\cdot}{\\cdot}{\\cdot}}')
        if SWITCHED or PyJsStrictEq(CONDITION, Js('....')):
            SWITCHED = True
            return Js('{{\\cdot}{\\cdot}{\\cdot}{\\cdot}}')
        if SWITCHED or PyJsStrictEq(CONDITION, Js('->')):
            SWITCHED = True
            return Js('{\\rightarrow}')
        if SWITCHED or PyJsStrictEq(CONDITION, Js('<-')):
            SWITCHED = True
            return Js('{\\leftarrow}')
        if SWITCHED or PyJsStrictEq(CONDITION, Js('<')):
            SWITCHED = True
            return Js('{<}')
        if SWITCHED or PyJsStrictEq(CONDITION, Js('>')):
            SWITCHED = True
            return Js('{>}')
        if True:
            SWITCHED = True
            var.get('assertNever')(var.get('a'))
            PyJsTempException = JsToPyException(Js([Js('MhchemBugT'), Js('mhchem bug T. Please report.')]))
            raise PyJsTempException
        SWITCHED = True
        break
PyJs_anonymous_123_._set_name('anonymous')
@Js
def PyJs_anonymous_124_(a, this, arguments, var=var):
    var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
    var.registers(['a'])
    while 1:
        SWITCHED = False
        CONDITION = (var.get('a'))
        if SWITCHED or PyJsStrictEq(CONDITION, Js('+')):
            SWITCHED = True
            return Js(' {}+{} ')
        if SWITCHED or PyJsStrictEq(CONDITION, Js('-')):
            SWITCHED = True
            return Js(' {}-{} ')
        if SWITCHED or PyJsStrictEq(CONDITION, Js('=')):
            SWITCHED = True
            return Js(' {}={} ')
        if SWITCHED or PyJsStrictEq(CONDITION, Js('<')):
            SWITCHED = True
            return Js(' {}<{} ')
        if SWITCHED or PyJsStrictEq(CONDITION, Js('>')):
            SWITCHED = True
            return Js(' {}>{} ')
        if SWITCHED or PyJsStrictEq(CONDITION, Js('<<')):
            SWITCHED = True
            return Js(' {}\\ll{} ')
        if SWITCHED or PyJsStrictEq(CONDITION, Js('>>')):
            SWITCHED = True
            return Js(' {}\\gg{} ')
        if SWITCHED or PyJsStrictEq(CONDITION, Js('\\pm')):
            SWITCHED = True
            return Js(' {}\\pm{} ')
        if SWITCHED or PyJsStrictEq(CONDITION, Js('\\approx')):
            SWITCHED = True
            return Js(' {}\\approx{} ')
        if SWITCHED or PyJsStrictEq(CONDITION, Js('$\\approx$')):
            SWITCHED = True
            return Js(' {}\\approx{} ')
        if SWITCHED or PyJsStrictEq(CONDITION, Js('v')):
            SWITCHED = True
            return Js(' \\downarrow{} ')
        if SWITCHED or PyJsStrictEq(CONDITION, Js('(v)')):
            SWITCHED = True
            return Js(' \\downarrow{} ')
        if SWITCHED or PyJsStrictEq(CONDITION, Js('^')):
            SWITCHED = True
            return Js(' \\uparrow{} ')
        if SWITCHED or PyJsStrictEq(CONDITION, Js('(^)')):
            SWITCHED = True
            return Js(' \\uparrow{} ')
        if True:
            SWITCHED = True
            var.get('assertNever')(var.get('a'))
            PyJsTempException = JsToPyException(Js([Js('MhchemBugT'), Js('mhchem bug T. Please report.')]))
            raise PyJsTempException
        SWITCHED = True
        break
PyJs_anonymous_124_._set_name('anonymous')
var.put('_mhchemTexify', Js({'go':PyJs_anonymous_119_,'_goInner':PyJs_anonymous_120_,'_go2':PyJs_anonymous_121_,'_getArrow':PyJs_anonymous_122_,'_getBond':PyJs_anonymous_123_,'_getOperator':PyJs_anonymous_124_}))
pass
pass


# Add lib to the module scope
mhchem = var.to_python()