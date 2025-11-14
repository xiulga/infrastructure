Building wheels for collected packages: asyncpg, pydantic-core
  Building wheel for asyncpg (pyproject.toml) ... error
  error: subprocess-exited-with-error
  
  × Building wheel for asyncpg (pyproject.toml) did not run successfully.
  │ exit code: 1
  ╰─> [236 lines of output]
      /private/var/folders/9d/stln9ycd27n41zvnjfjn33440000gn/T/pip-build-env-4ly2wgji/overlay/lib/python3.14/site-packages/setuptools/config/_apply_pyprojecttoml.py:82: SetuptoolsDeprecationWarning: `project.license` as a TOML table is deprecated
      !!
      
              ********************************************************************************
              Please use a simple string containing a SPDX expression for `project.license`. You can also use `project.license-files`. (Both options available on setuptools>=77.0.0).
      
              By 2026-Feb-18, you need to update your project and remove deprecated calls
              or your builds will no longer be supported.
      
              See https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#license for details.
              ********************************************************************************
      
      !!
        corresp(dist, value, root_dir)
      /private/var/folders/9d/stln9ycd27n41zvnjfjn33440000gn/T/pip-build-env-4ly2wgji/overlay/lib/python3.14/site-packages/setuptools/config/_apply_pyprojecttoml.py:61: SetuptoolsDeprecationWarning: License classifiers are deprecated.
      !!
      
              ********************************************************************************
              Please consider removing the following classifiers in favor of a SPDX license expression:
      
              License :: OSI Approved :: Apache Software License
      
              See https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#license for details.
              ********************************************************************************
      
      !!
        dist._finalize_license_expression()
      /private/var/folders/9d/stln9ycd27n41zvnjfjn33440000gn/T/pip-build-env-4ly2wgji/overlay/lib/python3.14/site-packages/setuptools/dist.py:759: SetuptoolsDeprecationWarning: License classifiers are deprecated.
      !!
      
              ********************************************************************************
              Please consider removing the following classifiers in favor of a SPDX license expression:
      
              License :: OSI Approved :: Apache Software License
      
              See https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#license for details.
              ********************************************************************************
      
      !!
        self._finalize_license_expression()
      running bdist_wheel
      running build
      running build_py
      creating build/lib.macosx-14.0-arm64-cpython-314/asyncpg
      copying asyncpg/compat.py -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg
      copying asyncpg/_version.py -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg
      copying asyncpg/transaction.py -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg
      copying asyncpg/__init__.py -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg
      copying asyncpg/types.py -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg
      copying asyncpg/serverversion.py -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg
      copying asyncpg/prepared_stmt.py -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg
      copying asyncpg/connection.py -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg
      copying asyncpg/utils.py -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg
      copying asyncpg/cluster.py -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg
      copying asyncpg/connect_utils.py -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg
      copying asyncpg/introspection.py -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg
      copying asyncpg/connresource.py -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg
      copying asyncpg/pool.py -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg
      copying asyncpg/_asyncio_compat.py -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg
      copying asyncpg/cursor.py -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg
      creating build/lib.macosx-14.0-arm64-cpython-314/asyncpg/_testbase
      copying asyncpg/_testbase/__init__.py -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg/_testbase
      copying asyncpg/_testbase/fuzzer.py -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg/_testbase
      creating build/lib.macosx-14.0-arm64-cpython-314/asyncpg/protocol
      copying asyncpg/protocol/__init__.py -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg/protocol
      creating build/lib.macosx-14.0-arm64-cpython-314/asyncpg/exceptions
      copying asyncpg/exceptions/_base.py -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg/exceptions
      copying asyncpg/exceptions/__init__.py -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg/exceptions
      creating build/lib.macosx-14.0-arm64-cpython-314/asyncpg/pgproto
      copying asyncpg/pgproto/__init__.py -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg/pgproto
      copying asyncpg/pgproto/types.py -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg/pgproto
      creating build/lib.macosx-14.0-arm64-cpython-314/asyncpg/protocol/codecs
      copying asyncpg/protocol/codecs/__init__.py -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg/protocol/codecs
      running egg_info
      writing asyncpg.egg-info/PKG-INFO
      writing dependency_links to asyncpg.egg-info/dependency_links.txt
      writing requirements to asyncpg.egg-info/requires.txt
      writing top-level names to asyncpg.egg-info/top_level.txt
      reading manifest file 'asyncpg.egg-info/SOURCES.txt'
      reading manifest template 'MANIFEST.in'
      warning: no files found matching '*.py' under directory 'examples'
      adding license file 'LICENSE'
      adding license file 'AUTHORS'
      writing manifest file 'asyncpg.egg-info/SOURCES.txt'
      copying asyncpg/protocol/consts.pxi -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg/protocol
      copying asyncpg/protocol/coreproto.pxd -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg/protocol
      copying asyncpg/protocol/coreproto.pyx -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg/protocol
      copying asyncpg/protocol/cpythonx.pxd -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg/protocol
      copying asyncpg/protocol/encodings.pyx -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg/protocol
      copying asyncpg/protocol/pgtypes.pxi -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg/protocol
      copying asyncpg/protocol/prepared_stmt.pxd -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg/protocol
      copying asyncpg/protocol/prepared_stmt.pyx -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg/protocol
      copying asyncpg/protocol/protocol.pxd -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg/protocol
      copying asyncpg/protocol/protocol.pyx -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg/protocol
      copying asyncpg/protocol/scram.pxd -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg/protocol
      copying asyncpg/protocol/scram.pyx -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg/protocol
      copying asyncpg/protocol/settings.pxd -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg/protocol
      copying asyncpg/protocol/settings.pyx -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg/protocol
      copying asyncpg/pgproto/__init__.pxd -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg/pgproto
      copying asyncpg/pgproto/buffer.pxd -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg/pgproto
      copying asyncpg/pgproto/buffer.pyx -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg/pgproto
      copying asyncpg/pgproto/consts.pxi -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg/pgproto
      copying asyncpg/pgproto/cpythonx.pxd -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg/pgproto
      copying asyncpg/pgproto/debug.pxd -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg/pgproto
      copying asyncpg/pgproto/frb.pxd -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg/pgproto
      copying asyncpg/pgproto/frb.pyx -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg/pgproto
      copying asyncpg/pgproto/hton.pxd -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg/pgproto
      copying asyncpg/pgproto/pgproto.pxd -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg/pgproto
      copying asyncpg/pgproto/pgproto.pyx -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg/pgproto
      copying asyncpg/pgproto/tohex.pxd -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg/pgproto
      copying asyncpg/pgproto/uuid.pyx -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg/pgproto
      copying asyncpg/protocol/codecs/array.pyx -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg/protocol/codecs
      copying asyncpg/protocol/codecs/base.pxd -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg/protocol/codecs
      copying asyncpg/protocol/codecs/base.pyx -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg/protocol/codecs
      copying asyncpg/protocol/codecs/pgproto.pyx -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg/protocol/codecs
      copying asyncpg/protocol/codecs/range.pyx -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg/protocol/codecs
      copying asyncpg/protocol/codecs/record.pyx -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg/protocol/codecs
      copying asyncpg/protocol/codecs/textutils.pyx -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg/protocol/codecs
      creating build/lib.macosx-14.0-arm64-cpython-314/asyncpg/protocol/record
      copying asyncpg/protocol/record/__init__.pxd -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg/protocol/record
      creating build/lib.macosx-14.0-arm64-cpython-314/asyncpg/pgproto/codecs
      copying asyncpg/pgproto/codecs/__init__.pxd -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg/pgproto/codecs
      copying asyncpg/pgproto/codecs/bits.pyx -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg/pgproto/codecs
      copying asyncpg/pgproto/codecs/bytea.pyx -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg/pgproto/codecs
      copying asyncpg/pgproto/codecs/context.pyx -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg/pgproto/codecs
      copying asyncpg/pgproto/codecs/datetime.pyx -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg/pgproto/codecs
      copying asyncpg/pgproto/codecs/float.pyx -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg/pgproto/codecs
      copying asyncpg/pgproto/codecs/geometry.pyx -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg/pgproto/codecs
      copying asyncpg/pgproto/codecs/hstore.pyx -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg/pgproto/codecs
      copying asyncpg/pgproto/codecs/int.pyx -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg/pgproto/codecs
      copying asyncpg/pgproto/codecs/json.pyx -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg/pgproto/codecs
      copying asyncpg/pgproto/codecs/jsonpath.pyx -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg/pgproto/codecs
      copying asyncpg/pgproto/codecs/misc.pyx -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg/pgproto/codecs
      copying asyncpg/pgproto/codecs/network.pyx -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg/pgproto/codecs
      copying asyncpg/pgproto/codecs/numeric.pyx -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg/pgproto/codecs
      copying asyncpg/pgproto/codecs/pg_snapshot.pyx -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg/pgproto/codecs
      copying asyncpg/pgproto/codecs/text.pyx -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg/pgproto/codecs
      copying asyncpg/pgproto/codecs/tid.pyx -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg/pgproto/codecs
      copying asyncpg/pgproto/codecs/uuid.pyx -> build/lib.macosx-14.0-arm64-cpython-314/asyncpg/pgproto/codecs
      running build_ext
      building 'asyncpg.pgproto.pgproto' extension
      creating build/temp.macosx-14.0-arm64-cpython-314/asyncpg/pgproto
      clang -fno-strict-overflow -Wsign-compare -Wunreachable-code -fno-common -dynamic -DNDEBUG -g -O3 -Wall -I/Users/k.shulga/PycharmProjects/xiulga/infrastructure/.venv/include -I/opt/homebrew/opt/python@3.14/Frameworks/Python.framework/Versions/3.14/include/python3.14 -c asyncpg/pgproto/pgproto.c -o build/temp.macosx-14.0-arm64-cpython-314/asyncpg/pgproto/pgproto.o -O2 -fsigned-char -Wall -Wsign-compare -Wconversion
      asyncpg/pgproto/pgproto.c:864:59: warning: 'Py_UNICODE' is deprecated [-Wdeprecated-declarations]
      static CYTHON_INLINE size_t __Pyx_Py_UNICODE_strlen(const Py_UNICODE *u) {
                                                                ^
      /opt/homebrew/opt/python@3.14/Frameworks/Python.framework/Versions/3.14/include/python3.14/cpython/unicodeobject.h:10:1: note: 'Py_UNICODE' has been explicitly marked deprecated here
      Py_DEPRECATED(3.13) typedef wchar_t Py_UNICODE;
      ^
      /opt/homebrew/opt/python@3.14/Frameworks/Python.framework/Versions/3.14/include/python3.14/pyport.h:280:54: note: expanded from macro 'Py_DEPRECATED'
      #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                           ^
      asyncpg/pgproto/pgproto.c:865:11: warning: 'Py_UNICODE' is deprecated [-Wdeprecated-declarations]
          const Py_UNICODE *u_end = u;
                ^
      /opt/homebrew/opt/python@3.14/Frameworks/Python.framework/Versions/3.14/include/python3.14/cpython/unicodeobject.h:10:1: note: 'Py_UNICODE' has been explicitly marked deprecated here
      Py_DEPRECATED(3.13) typedef wchar_t Py_UNICODE;
      ^
      /opt/homebrew/opt/python@3.14/Frameworks/Python.framework/Versions/3.14/include/python3.14/pyport.h:280:54: note: expanded from macro 'Py_DEPRECATED'
      #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                           ^
      asyncpg/pgproto/pgproto.c:1667:39: error: call to undeclared function '_PyInterpreterState_GetConfig'; ISO C99 and later do not support implicit function declarations [-Wimplicit-function-declaration]
          __pyx_assertions_enabled_flag = ! _PyInterpreterState_GetConfig(__Pyx_PyThreadState_Current->interp)->optimization_level;
                                            ^
      asyncpg/pgproto/pgproto.c:1667:107: error: member reference type 'int' is not a pointer
          __pyx_assertions_enabled_flag = ! _PyInterpreterState_GetConfig(__Pyx_PyThreadState_Current->interp)->optimization_level;
                                            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  ^
      asyncpg/pgproto/pgproto.c:38932:13: error: call to undeclared function '_PyUnicode_FastCopyCharacters'; ISO C99 and later do not support implicit function declarations [-Wimplicit-function-declaration]
                  _PyUnicode_FastCopyCharacters(result_uval, char_pos, uval, 0, ulength);
                  ^
      asyncpg/pgproto/pgproto.c:38932:13: note: did you mean 'PyUnicode_CopyCharacters'?
      /opt/homebrew/opt/python@3.14/Frameworks/Python.framework/Versions/3.14/include/python3.14/cpython/unicodeobject.h:435:24: note: 'PyUnicode_CopyCharacters' declared here
      PyAPI_FUNC(Py_ssize_t) PyUnicode_CopyCharacters(
                             ^
      asyncpg/pgproto/pgproto.c:41811:70: error: too few arguments to function call, expected 6, have 5
                                                    is_little, !is_unsigned);
                                                                           ^
      /opt/homebrew/opt/python@3.14/Frameworks/Python.framework/Versions/3.14/include/python3.14/cpython/longobject.h:84:17: note: '_PyLong_AsByteArray' declared here
      PyAPI_FUNC(int) _PyLong_AsByteArray(PyLongObject* v,
                      ^
      asyncpg/pgproto/pgproto.c:42045:70: error: too few arguments to function call, expected 6, have 5
                                                    is_little, !is_unsigned);
                                                                           ^
      /opt/homebrew/opt/python@3.14/Frameworks/Python.framework/Versions/3.14/include/python3.14/cpython/longobject.h:84:17: note: '_PyLong_AsByteArray' declared here
      PyAPI_FUNC(int) _PyLong_AsByteArray(PyLongObject* v,
                      ^
      asyncpg/pgproto/pgproto.c:42241:70: error: too few arguments to function call, expected 6, have 5
                                                    is_little, !is_unsigned);
                                                                           ^
      /opt/homebrew/opt/python@3.14/Frameworks/Python.framework/Versions/3.14/include/python3.14/cpython/longobject.h:84:17: note: '_PyLong_AsByteArray' declared here
      PyAPI_FUNC(int) _PyLong_AsByteArray(PyLongObject* v,
                      ^
      asyncpg/pgproto/pgproto.c:42437:70: error: too few arguments to function call, expected 6, have 5
                                                    is_little, !is_unsigned);
                                                                           ^
      /opt/homebrew/opt/python@3.14/Frameworks/Python.framework/Versions/3.14/include/python3.14/cpython/longobject.h:84:17: note: '_PyLong_AsByteArray' declared here
      PyAPI_FUNC(int) _PyLong_AsByteArray(PyLongObject* v,
                      ^
      asyncpg/pgproto/pgproto.c:42747:70: error: too few arguments to function call, expected 6, have 5
                                                    is_little, !is_unsigned);
                                                                           ^
      /opt/homebrew/opt/python@3.14/Frameworks/Python.framework/Versions/3.14/include/python3.14/cpython/longobject.h:84:17: note: '_PyLong_AsByteArray' declared here
      PyAPI_FUNC(int) _PyLong_AsByteArray(PyLongObject* v,
                      ^
      asyncpg/pgproto/pgproto.c:43057:70: error: too few arguments to function call, expected 6, have 5
                                                    is_little, !is_unsigned);
                                                                           ^
      /opt/homebrew/opt/python@3.14/Frameworks/Python.framework/Versions/3.14/include/python3.14/cpython/longobject.h:84:17: note: '_PyLong_AsByteArray' declared here
      PyAPI_FUNC(int) _PyLong_AsByteArray(PyLongObject* v,
                      ^
      asyncpg/pgproto/pgproto.c:43291:70: error: too few arguments to function call, expected 6, have 5
                                                    is_little, !is_unsigned);
                                                                           ^
      /opt/homebrew/opt/python@3.14/Frameworks/Python.framework/Versions/3.14/include/python3.14/cpython/longobject.h:84:17: note: '_PyLong_AsByteArray' declared here
      PyAPI_FUNC(int) _PyLong_AsByteArray(PyLongObject* v,
                      ^
      asyncpg/pgproto/pgproto.c:43487:70: error: too few arguments to function call, expected 6, have 5
                                                    is_little, !is_unsigned);
                                                                           ^
      /opt/homebrew/opt/python@3.14/Frameworks/Python.framework/Versions/3.14/include/python3.14/cpython/longobject.h:84:17: note: '_PyLong_AsByteArray' declared here
      PyAPI_FUNC(int) _PyLong_AsByteArray(PyLongObject* v,
                      ^
      asyncpg/pgproto/pgproto.c:43721:70: error: too few arguments to function call, expected 6, have 5
                                                    is_little, !is_unsigned);
                                                                           ^
      /opt/homebrew/opt/python@3.14/Frameworks/Python.framework/Versions/3.14/include/python3.14/cpython/longobject.h:84:17: note: '_PyLong_AsByteArray' declared here
      PyAPI_FUNC(int) _PyLong_AsByteArray(PyLongObject* v,
                      ^
      asyncpg/pgproto/pgproto.c:43917:70: error: too few arguments to function call, expected 6, have 5
                                                    is_little, !is_unsigned);
                                                                           ^
      /opt/homebrew/opt/python@3.14/Frameworks/Python.framework/Versions/3.14/include/python3.14/cpython/longobject.h:84:17: note: '_PyLong_AsByteArray' declared here
      PyAPI_FUNC(int) _PyLong_AsByteArray(PyLongObject* v,
                      ^
      2 warnings and 13 errors generated.
      error: command '/usr/bin/clang' failed with exit code 1
      [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for asyncpg
  Building wheel for pydantic-core (pyproject.toml) ... error                                                                                                                                  
  error: subprocess-exited-with-error
  
  × Building wheel for pydantic-core (pyproject.toml) did not run successfully.
  │ exit code: 1
  ╰─> [107 lines of output]
      Running `maturin pep517 build-wheel -i /Users/k.shulga/PycharmProjects/xiulga/infrastructure/.venv/bin/python --compatibility off`
      Python reports SOABI: cpython-314-darwin
      Computed rustc target triple: aarch64-apple-darwin
      Installation directory: /Users/k.shulga/Library/Caches/puccinialin
      Rustup already downloaded
      Installing rust to /Users/k.shulga/Library/Caches/puccinialin/rustup
      warn: It looks like you have an existing rustup settings file at:
      warn: /Users/k.shulga/.rustup/settings.toml
      warn: Rustup will install the default toolchain as specified in the settings file,
      warn: instead of the one inferred from the default host triple.
      info: profile set to 'minimal'
      info: default host triple is aarch64-apple-darwin
      warn: Updating existing toolchain, profile choice will be ignored
      info: syncing channel updates for 'stable-aarch64-apple-darwin'
      info: default toolchain set to 'stable-aarch64-apple-darwin'
      Checking if cargo is installed
      cargo 1.91.1 (ea2d97820 2025-10-10)
      📦 Including license file `LICENSE`
      🍹 Building a mixed python/rust project
      🔗 Found pyo3 bindings
      🐍 Found CPython 3.14 at /Users/k.shulga/PycharmProjects/xiulga/infrastructure/.venv/bin/python
      📡 Using build options features, bindings from pyproject.toml
      💻 Using `MACOSX_DEPLOYMENT_TARGET=11.0` for aarch64-apple-darwin by default
         Compiling target-lexicon v0.12.14
         Compiling python3-dll-a v0.2.10
         Compiling once_cell v1.19.0
         Compiling proc-macro2 v1.0.86
         Compiling unicode-ident v1.0.12
         Compiling autocfg v1.3.0
         Compiling libc v0.2.155
         Compiling heck v0.5.0
         Compiling version_check v0.9.4
         Compiling rustversion v1.0.17
         Compiling static_assertions v1.1.0
         Compiling radium v0.7.0
         Compiling tinyvec_macros v0.1.1
         Compiling num-traits v0.2.19
         Compiling memoffset v0.9.1
         Compiling cfg-if v1.0.0
         Compiling ahash v0.8.11
         Compiling tinyvec v1.6.1
         Compiling pyo3-build-config v0.22.0
         Compiling lexical-util v0.8.5
         Compiling quote v1.0.36
         Compiling syn v2.0.68
         Compiling memchr v2.7.4
         Compiling tap v1.0.1
         Compiling serde v1.0.203
         Compiling lexical-parse-integer v0.8.6
         Compiling wyz v0.5.1
         Compiling aho-corasick v1.1.3
         Compiling getrandom v0.2.15
         Compiling unicode-normalization v0.1.23
         Compiling num-integer v0.1.46
         Compiling equivalent v1.0.1
         Compiling num-bigint v0.4.6
         Compiling percent-encoding v2.3.1
         Compiling unindent v0.2.3
         Compiling unicode-bidi v0.3.15
         Compiling funty v2.0.0
         Compiling serde_json v1.0.118
         Compiling indoc v2.0.5
         Compiling regex-syntax v0.8.4
         Compiling pyo3-macros-backend v0.22.0
         Compiling pyo3-ffi v0.22.0
         Compiling pyo3 v0.22.0
         Compiling jiter v0.5.0
         Compiling zerocopy v0.7.34
         Compiling hashbrown v0.14.5
      error: failed to run custom build command for `pyo3-ffi v0.22.0`
      
      Caused by:
        process didn't exit successfully: `/private/var/folders/9d/stln9ycd27n41zvnjfjn33440000gn/T/pip-install-xmvba0nl/pydantic-core_6e2598ddb5a14b6c99a70c1c61fb477c/target/release/build/pyo3-ffi-b47f4eb7e1d4775c/build-script-build` (exit status: 1)
        --- stdout
        cargo:rustc-check-cfg=cfg(Py_LIMITED_API)
        cargo:rustc-check-cfg=cfg(PyPy)
        cargo:rustc-check-cfg=cfg(GraalPy)
        cargo:rustc-check-cfg=cfg(py_sys_config, values("Py_DEBUG", "Py_REF_DEBUG", "Py_TRACE_REFS", "COUNT_ALLOCS"))
        cargo:rustc-check-cfg=cfg(invalid_from_utf8_lint)
        cargo:rustc-check-cfg=cfg(pyo3_disable_reference_pool)
        cargo:rustc-check-cfg=cfg(pyo3_leak_on_drop_without_reference_pool)
        cargo:rustc-check-cfg=cfg(diagnostic_namespace)
        cargo:rustc-check-cfg=cfg(c_str_lit)
        cargo:rustc-check-cfg=cfg(Py_3_7)
        cargo:rustc-check-cfg=cfg(Py_3_8)
        cargo:rustc-check-cfg=cfg(Py_3_9)
        cargo:rustc-check-cfg=cfg(Py_3_10)
        cargo:rustc-check-cfg=cfg(Py_3_11)
        cargo:rustc-check-cfg=cfg(Py_3_12)
        cargo:rustc-check-cfg=cfg(Py_3_13)
        cargo:rerun-if-env-changed=PYO3_CROSS
        cargo:rerun-if-env-changed=PYO3_CROSS_LIB_DIR
        cargo:rerun-if-env-changed=PYO3_CROSS_PYTHON_VERSION
        cargo:rerun-if-env-changed=PYO3_CROSS_PYTHON_IMPLEMENTATION
        cargo:rerun-if-env-changed=PYO3_PRINT_CONFIG
        cargo:rerun-if-env-changed=PYO3_USE_ABI3_FORWARD_COMPATIBILITY
      
        --- stderr
        error: the configured Python interpreter version (3.14) is newer than PyO3's maximum supported version (3.13)
        = help: please check if an updated version of PyO3 is available. Current version: 0.22.0
        = help: set PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1 to suppress this check and build anyway using the stable ABI
      warning: build failed, waiting for other jobs to finish...
      💥 maturin failed
        Caused by: Failed to build a native library through cargo
        Caused by: Cargo build finished with "exit status: 101": `env -u CARGO MACOSX_DEPLOYMENT_TARGET="11.0" PYO3_BUILD_EXTENSION_MODULE="1" PYO3_ENVIRONMENT_SIGNATURE="cpython-3.14-64bit" PYO3_PYTHON="/Users/k.shulga/PycharmProjects/xiulga/infrastructure/.venv/bin/python" PYTHON_SYS_EXECUTABLE="/Users/k.shulga/PycharmProjects/xiulga/infrastructure/.venv/bin/python" "cargo" "rustc" "--profile" "release" "--features" "pyo3/extension-module" "--message-format" "json-render-diagnostics" "--manifest-path" "/private/var/folders/9d/stln9ycd27n41zvnjfjn33440000gn/T/pip-install-xmvba0nl/pydantic-core_6e2598ddb5a14b6c99a70c1c61fb477c/Cargo.toml" "--lib" "--crate-type" "cdylib" "--" "-C" "link-arg=-undefined" "-C" "link-arg=dynamic_lookup" "-C" "link-args=-Wl,-install_name,@rpath/pydantic_core._pydantic_core.cpython-314-darwin.so"`
      Rust not found, installing into a temporary directory
      Error: command ['maturin', 'pep517', 'build-wheel', '-i', '/Users/k.shulga/PycharmProjects/xiulga/infrastructure/.venv/bin/python', '--compatibility', 'off'] returned non-zero exit status 1
      [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for pydantic-core
Failed to build asyncpg pydantic-core                                                                                                                                                          
error: failed-wheel-build-for-install

× Failed to build installable wheels for some pyproject.toml based projects
╰─> asyncpg, pydantic-core