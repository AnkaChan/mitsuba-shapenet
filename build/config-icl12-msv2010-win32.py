import sys, os

BUILDDIR       = '#build/release'
DISTDIR        = '#dist'
CXX            = 'icl'
CC             = 'icl'
LINK           = 'xilink'
CXXFLAGS       = ['/nologo', '/O3', '/Qipo', '/QxSSE2', '/QaxSSE3,SSE4.2', '/fp:fast=2', '/D', 'WIN32', '/W3', '/Qdiag-disable:2586', '/EHsc', '/GS-', '/MD', '/D', 'MTS_DEBUG', '/D', 'SINGLE_PRECISION', '/D', 'SPECTRUM_SAMPLES=3', '/D', 'MTS_SSE', '/D', 'MTS_HAS_COHERENT_RT', '/D', '_CONSOLE', '/D', 'NDEBUG', '/Qopenmp']
SHCXXFLAGS     = CXXFLAGS
TARGET_ARCH    = 'x86'
MSVC_VERSION   = '10.0'
INTEL_COMPILER = True
LINKFLAGS      = ['/nologo', '/SUBSYSTEM:CONSOLE', '/MACHINE:X86', '/FIXED:NO', '/OPT:REF', '/OPT:ICF', '/NODEFAULTLIB:LIBCMT', '/MANIFEST', '/Qdiag-disable:11024']
BASEINCLUDE    = ['#include', '#dependencies/windows/include']
BASELIB        = ['pthreadVCE2', 'msvcrt', 'ws2_32']
OEXRINCLUDE    = ['#dependencies/windows/include/OpenEXR']
OEXRFLAGS      = ['/D', 'OPENEXR_DLL']
OEXRLIB        = ['IlmImf', 'IlmThread', 'zlib1', 'Half']
BOOSTINCLUDE   = ['#dependencies']
BOOSTLIB       = ['boost_system-vc100-mt-1_44', 'boost_filesystem-vc100-mt-1_44']
COLLADAINCLUDE = ['#dependencies/windows/include/colladadom', '#dependencies/windows/include/colladadom/1.4']
COLLADALIB     = ['libcollada14dom23']
XERCESLIB      = ['xerces-c_3']
PNGLIB         = ['libpng13']
JPEGLIB        = ['jpeg62']
GLLIB          = ['opengl32', 'glu32', 'glew32mx', 'gdi32', 'user32']
GLFLAGS        = ['/D', 'GLEW_MX']
BASELIBDIR     = ['#dependencies/windows/lib32', '#dependencies/windows/lib32/vc100']
PYTHONINCLUDE  = [os.path.join(os.path.split(sys.executable)[0], 'include')]
PYTHONLIBDIR   = [os.path.join(os.path.split(sys.executable)[0], 'libs')]
PYTHONLIB      = ['boost_python-vc100-mt-1_44']
SHLIBPREFIX    = 'lib'
SHLIBSUFFIX    = '.dll'
PROGSUFFIX     = '.exe'
